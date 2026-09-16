# Article playbook — how a new post gets written and shipped on lawnandlandmarketing.com

This is the standard for every new article, whether a person or the scheduled SEO routine
writes it. It exists so nothing that reads like generic AI filler ever lands on this blog.
Read `CONTENT-QUEUE.md` for what to write next and `STRATEGY.md` for why.

## 0. Who reads this blog
Owners and managers of green-industry companies: landscapers (priority 1), outdoor living /
hardscape contractors (2), land clearing companies (3), then excavation, lawn care, lawn
maintenance, septic installers. Never write for homeowners. Every article answers a question
an owner would ask, in an operator's voice, from Lawn & Land's real experience.

## 1. Non-negotiables (violating any one = do not publish)
- **Inform, do not pitch.** Teach the topic completely. Lawn & Land appears once, in the CTA
  block, and where a real client example is genuinely the best illustration.
- **No invented facts.** Every number has a primary source linked inline (Google documentation,
  BLS, IRS, NALP, state licensing boards, a named industry report). If a figure cannot be
  sourced, leave it out. Never fabricate quotes, clients, or results.
- **Real examples only.** Client examples are limited to what is already published on this
  site: the Precision Landscape Management and Rock Solid Landscape case studies, and the
  owner stories in the podcast recaps. Never name a private customer of a client.
- **Only Lawn & Land's 8 services** may be referenced as things we do: website design, local
  SEO, Google Ads, Meta Ads, GBP management, AI partner, reputation management, CRM and
  automation. Never imply we run a client's sales, renewals, hiring, or operations.
- **No pricing** for our services. Industry cost ranges with a source are fine.
- **Style:** no em dashes. City or county names carry a 2-letter state code ("Tampa, FL").
  Plain words, specific claims, short paragraphs. No "in today's fast-paced world", no
  "unlock", "elevate", "game-changer", "delve", "landscape" as a metaphor, no rhetorical
  question openers, no summary paragraphs that restate the section.
- **No geo pages, no "near me" pages, no snow removal.**
- **One article per target keyword.** Before writing, grep `_blog.json` titles and the site
  for the target term and its close variants. If a post already covers it, improve and
  interlink that post instead of writing a duplicate.

## 2. What makes an article worth publishing
1. **A point of view.** Say what most guides get wrong about the topic and why. Draw on the
   agency's operating experience (seasonality, route density, high-ticket sales cycles, the
   difference between a lead and a booked job).
2. **An original framework or checklist** the reader can act on this week.
3. **Answer-first structure.** Each H2 is the question an owner would type; the first
   sentence under it is the answer. AI Overviews and featured snippets lift exactly this.
4. **Specifics over adjectives.** Ranges, timelines, step counts, named tools, named sources.
5. **A worked example** with numbers (sourced or clearly labeled as an illustration).
6. **1,800 to 2,500 words.** Long enough to be complete, never padded.

## 3. Research before writing (30 minutes, not 3)
- Pull the live Google SERP for the target keyword (DataForSEO `serp/google/organic/live/advanced`
  if credentials are present, otherwise WebSearch). Note what the top 5 cover, what the
  People Also Ask box asks, and whether an AI Overview appears.
- Read 2 to 3 of the top results. Your article must cover what they cover and add what
  they miss. Write down the 3 things they miss; those become sections.
- Collect 2 to 4 primary sources with URLs before writing a word.

## 4. Structure (copy `resources/blog/lawn-care-seo-recurring-revenue/index.html` as the template)
Head: `<title>` = `seoTitle`; description ≤ 155 chars; canonical; og:/twitter: tags; BlogPosting
JSON-LD with `datePublished`, `dateModified`, `image`, author `@id` `#matt-foreman`,
publisher `@id` `#organization`. Every URL absolute on `https://lawnandlandmarketing.com`.

Body, in order:
1. `article-hero`: badge (category label), H1 (the human title, may be longer than seoTitle),
   author block (Matt Foreman), date, read time, `<figure class="article-hero-img">`
   (gen_blog stamps the image; leave the placeholder figure in place).
2. `article-lead`: 2 short paragraphs. State the problem and the point of view.
3. `Key takeaways` section: 4 bullets, each a complete, specific claim.
4. 5 to 7 `<section>` blocks, each `<h2>` a question, answer-first opener, 150 to 350 words,
   at least one list or table where it helps scanning. One section holds the worked example.
5. `article-cta-block` with the contextual line
   `<p class="article-cta-link">Want this done for you? See our <a href="...">… service</a>.</p>`
   pointing at the matching vertical service page or industry page.
6. `Frequently asked questions`: 4 to 6 `<div class="faq-item"><h3>Q?</h3><p>A.</p></div>`
   (gen_blog_schema turns these into FAQPage schema; keep the exact markup).
7. Author block (unchanged from template).
Aside: keep the template's form and update the two "Related reading" links to the most
relevant posts or case studies.

Internal links inside the body: 3 to 6, descriptive anchors, to the priority industry page,
the vertical service page, and 1 to 3 related posts. External links: the primary sources,
`rel="noopener"`.

## 5. Images (gpt-image-2 only, never gpt-image-1)
- Hero via `python3 scripts/gen_photos.py --slug <slug> --prompt "<scene>" --variant "<style>"`.
  Write a scene specific to the article (not the generic topic mapping), photoreal, no text,
  no logos, no readable faces, landscape orientation. Rotate the style across posts so the
  blog does not look like one shoot: documentary crew shot, overhead drone, golden hour,
  close detail of hands and materials, blue-hour with equipment lights, overcast workshop,
  planning desk with plans. Check the last five posts' images before choosing.
- Output lands at `assets/images/blog/photos/<slug>.webp` (1200×630, ≤ 150 KB).
- Alt text describes the scene in plain words, never the keyword stuffed in.
- Optional one in-body `<figure>` when a diagram or table screenshot genuinely helps. Never
  decorative filler.

## 6. Ship checklist (all must pass)
```bash
# 1. _blog.json: add the entry at the TOP of "posts" (newest first):
#    slug, title, seoTitle (≤60 chars), excerpt (≤160), datePublished (YYYY-MM-DD),
#    dateDisplay ("September 18, 2026"), badge (Strategy | SEO | Ads & Social | Owner Stories),
#    cat (strategy | seo | ads-social | growth-stories), readTime, image, imageAlt, video: null
python3 gen_blog.py && python3 gen_blog_schema.py && python3 build.py && python3 build.py --check
# 2. sitemap.xml is hand-kept: add one <url> line for the new post in the blog block
python3 scripts/check_links.py && python3 scripts/check_structured_data.py && python3 scripts/check_blog_images.py && python3 scripts/check_seo_migration_fixes.py
# 3. Re-read the article once as the owner it is written for. Cut anything that sounds like a robot.
```
Commit on a branch `seo/<slug>`, open a PR titled `seo: <title>` whose body lists the target
keyword, volume, the sources used, the internal links added, and the image prompt. **Merge
rule:** the PR auto-merges on the next scheduled run if it is still open after 24 hours;
closing the PR is the veto. If the Competitor Radar ledger credentials are available
(`CI_SUPABASE_URL` + `CI_SUPABASE_KEY`), insert a `ci_operator_actions` row with play
`MANUAL` for the slug so the radar's duplicate-target guard can see it.

## 7. After publishing
- Add the post to `CONTENT-QUEUE.md` as done (with date and URL).
- Link to the new post from 1 to 2 older posts on the same topic (edit their body copy, not
  the CTA block) so it is not an orphan.
- The Monday review routine watches its impressions in Search Console.
