# Blog Migration Spec (legacy WordPress post → new article)

Migrate ONE legacy post into the new blog at `/resources/blog/<slug>/`, matching the canonical
template EXACTLY so every article is visually + structurally consistent and nothing breaks.

## Canonical template — COPY THIS FILE'S STRUCTURE
`resources/blog/why-landscaping-seo-gets-traffic-not-qualified-leads/index.html`

Read it first. Your output must be identical to it **except** the clearly-variable regions below.
Keep UNCHANGED: every class name, the announcement bar + `<nav>`, the `<footer class="footer-v2">`,
the inline `<style>` block, the sidebar (`#contactForm` + its `<script>` + the GHL webhook URL + the
related-reading card with the 2 case studies), the `.author-block` (Matt bio), the CSS/JS version
links (`styles.css?v=142`, `article.css?v=7`, `main.js?v=56`). `build.py` re-stamps the nav/footer on
deploy, so just keep them present.

## Source
`curl -s https://lawnandlandmarketing.com/blog/<OLD_SLUG>/`
- Extract the REAL `datePublished` (page JSON-LD, or `<meta property="article:published_time">`). PRESERVE IT EXACTLY.
- Extract the real article content (headings, paragraphs, lists, any real quotes/numbers).
- If the source contains AI production notes, leaked instructions, or a copy-pasted-wrong intro, do
  NOT carry it over. Clean it and record in `issues`.

## Output
Write `resources/blog/<SLUG>/index.html`. SLUG = OLD_SLUG, unchanged (keeps the redirect clean).

## Variable regions (replace these; everything else identical to template)
1. **`<head>`**
   - `<title>` ~55-60 chars + ` | Lawn &amp; Land Marketing`.
   - meta description ~155 chars.
   - `canonical` + `og:url` = `https://new.lawnlab.dev/resources/blog/<SLUG>/` (STAGING — match template).
   - og/twitter title + description.
   - **BlogPosting JSON-LD**: headline, description, `datePublished` = REAL date, `dateModified` = same,
     `url` + `mainEntityOfPage` = `https://lawnandlandmarketing.com/resources/blog/<SLUG>/`
     (PRODUCTION domain in schema — match template), author `#matt-foreman`, publisher `#organization`.
   - **FAQPage JSON-LD**: 3-4 genuinely useful Q&As for the topic — OR remove the FAQPage script AND the
     FAQ section together if FAQs don't fit (e.g. a client story).
2. **Hero (`.article-hero`)**
   - breadcrumb last `<span>` = short title.
   - `.article-category-badge` = the BADGE you're given.
   - `.article-headline` = the H1, with ONE 2-5 word emphasis phrase wrapped in `<em>`.
   - `.article-author` block UNCHANGED.
   - `.article-date` = "Month D, YYYY" (REAL date). `.article-read-time` = realistic "N min read".
   - `.article-hero-img` → `<figure class="article-hero-img"><div class="img-ph" style="width:100%;height:420px;"></div></figure>`
     (placeholder; real image added later by the image pass).
3. **`.article-content`**
   - `.article-lead` = strong 1-2 sentence opener.
   - Body: faithful migration, in `<section>` blocks with `<h2>`/`<h3>`/`<p>`/`<ul>`/`<blockquote>`.
     Cut AI-filler fluff; keep the real substance, real tools, real numbers (only if in the source).
   - Keep `.article-cta-block` (tailor its `<h3>` + `<p>` to the topic; button → `/get-started/book-strategy-call/`;
     use only "20-minute strategy call" when referring to the booking CTA. Do not use older duration variants).
   - FAQ `<section>` + `.article-faq` must match the FAQPage schema (or remove both).
   - `.author-block` UNCHANGED.
4. **Sidebar (`.article-aside`)** UNCHANGED.

## Brand rules (HARD)
- NO em-dashes (—). Use periods, commas, or parentheses.
- NO pricing anywhere. Every CTA → `/get-started/book-strategy-call/`.
- Do NOT fabricate facts, quotes, numbers, or client results. For client-story posts, migrate only the
  guest's REAL story from the source; if a number/quote isn't in the source, omit it.
- Town/city names carry a 2-letter state code ("St. Louis, MO").
- Lucide stroke icons only; never emoji.
- Author = Matt Foreman (`/author/matt-foreman/`); first-person voice OK.

## Return (SHORT — do NOT paste the article body)
Return ONLY a compact JSON object:
`{"slug","title","headline","excerpt"(~22 words for the index card),"datePublished","dateDisplay","readTime","badge","dataCat","faqIncluded","heroImageNeeded":true,"issues"}`
