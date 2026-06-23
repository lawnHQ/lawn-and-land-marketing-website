import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.4";
import { jwtVerify, createRemoteJWKSet } from "https://esm.sh/jose@5.9.6";

// Custom auth: every request must carry a valid Google ID token from a
// @lawnandlandmarketing.com Workspace account. verify_jwt is disabled because we
// verify the Google token ourselves (not a Supabase JWT). Every create/update/delete
// is written to the append-only audit_log (who / what / when).
const GOOGLE_CLIENT_ID = "719731442715-5f1tdlaqgnfmpc1o72l2endva1iia4s2.apps.googleusercontent.com";
const ALLOWED_DOMAIN = "lawnandlandmarketing.com";
const JWKS = createRemoteJWKSet(new URL("https://www.googleapis.com/oauth2/v3/certs"));

const CORS: Record<string, string> = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, content-type",
  "Access-Control-Allow-Methods": "GET, POST, PATCH, DELETE, OPTIONS",
};
const json = (o: unknown, s = 200) =>
  new Response(JSON.stringify(o), { status: s, headers: { ...CORS, "content-type": "application/json" } });

async function getUser(req: Request): Promise<string | null> {
  const token = (req.headers.get("authorization") || "").replace(/^Bearer\s+/i, "").trim();
  if (!token) return null;
  try {
    const { payload } = await jwtVerify(token, JWKS, {
      issuer: ["https://accounts.google.com", "accounts.google.com"],
      audience: GOOGLE_CLIENT_ID,
    });
    const email = String(payload.email || "").toLowerCase();
    if (payload.email_verified !== true) return null;
    if (payload.hd !== ALLOWED_DOMAIN && !email.endsWith("@" + ALLOWED_DOMAIN)) return null;
    return email;
  } catch (_e) {
    return null;
  }
}

const cleanSlug = (s: string) => String(s || "").trim().toLowerCase().replace(/^\/+|\/+$/g, "");

// deno-lint-ignore no-explicit-any
async function logChange(supabase: any, actor: string, action: string, redirectId: string | null, slug: string, changes: unknown) {
  try {
    await supabase.from("audit_log").insert({ actor, action, redirect_id: redirectId, slug, changes });
  } catch (_e) { /* best-effort; never block the change itself */ }
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const email = await getUser(req);
  if (!email) return json({ error: "Unauthorized — sign in with your Lawn & Land Google account." }, 401);

  const supabase = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);

  try {
    if (req.method === "GET") {
      if (new URL(req.url).searchParams.get("view") === "log") {
        const { data, error } = await supabase.from("audit_log").select("*").order("at", { ascending: false }).limit(300);
        if (error) throw error;
        return json({ log: data, user: email });
      }
      const { data, error } = await supabase.from("redirects").select("*").order("slug");
      if (error) throw error;
      return json({ redirects: data, user: email });
    }

    // deno-lint-ignore no-explicit-any
    const body = await req.json().catch(() => ({} as any));

    if (req.method === "POST") {
      const row = {
        slug: cleanSlug(body.slug),
        destination: String(body.destination || "").trim(),
        active: body.active ?? true,
        category: body.category || null,
        notes: body.notes || null,
      };
      if (!row.slug || !row.destination) return json({ error: "Slug and destination are required." }, 400);
      const { data, error } = await supabase.from("redirects").insert(row).select().single();
      if (error) return json({ error: error.code === "23505" ? "That slug already exists." : error.message }, 400);
      await logChange(supabase, email, "create", data.id, data.slug, { destination: data.destination, active: data.active, category: data.category, notes: data.notes });
      return json({ redirect: data });
    }

    if (req.method === "PATCH") {
      if (!body.id) return json({ error: "Missing id." }, 400);
      const { data: before } = await supabase.from("redirects").select("*").eq("id", body.id).single();
      const patch: Record<string, unknown> = {};
      for (const k of ["slug", "destination", "active", "category", "notes"]) {
        if (k in body) patch[k] = k === "slug" ? cleanSlug(body[k]) : body[k];
      }
      const { data, error } = await supabase.from("redirects").update(patch).eq("id", body.id).select().single();
      if (error) return json({ error: error.code === "23505" ? "That slug already exists." : error.message }, 400);
      const diff: Record<string, unknown> = {};
      if (before) {
        for (const k of ["slug", "destination", "active", "category", "notes"]) {
          // deno-lint-ignore no-explicit-any
          if ((before as any)[k] !== (data as any)[k]) diff[k] = { from: (before as any)[k], to: (data as any)[k] };
        }
      }
      if (Object.keys(diff).length) await logChange(supabase, email, "update", data.id, data.slug, diff);
      return json({ redirect: data });
    }

    if (req.method === "DELETE") {
      const id = new URL(req.url).searchParams.get("id") || body.id;
      if (!id) return json({ error: "Missing id." }, 400);
      const { data: before } = await supabase.from("redirects").select("*").eq("id", id).single();
      const { error } = await supabase.from("redirects").delete().eq("id", id);
      if (error) throw error;
      await logChange(supabase, email, "delete", id, before?.slug || "(unknown)", { destination: before?.destination, active: before?.active, category: before?.category, notes: before?.notes });
      return json({ ok: true });
    }

    return json({ error: "Method not allowed." }, 405);
  } catch (e) {
    return json({ error: String((e as Error)?.message || e) }, 400);
  }
});
