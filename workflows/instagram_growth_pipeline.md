# Instagram Growth Pipeline

## Objective
Grow @the_shedstudio on Instagram from its current 71-follower baseline
toward a 10,000-follower target within 30 days by publishing near-daily
AI-generated Reels across 5 proven content pillars, and by tracking real
performance data via Sandcastles now that the account is verified and
watchlisted.

## Current strategy (locked 2026-08-10)
Full competitive research and the 30-day plan live in the Google Doc
**"Instagram Growth Plan: @the_shedstudio to 10K in 30 Days"**:
https://docs.google.com/document/d/1lwDmTssCu9MyO7UdK0DXNJmdQu0MBGoaKLZuLWAYkzk/edit

Niche: AI-generated viral videos — hip hop, anime, dance culture, pop
culture. Built from live Instagram creator/video data pulled via the
Sandcastles MCP server, studying 5 real accounts (`@evolving.ai`,
`@airesearches`, `@mrbankzzzz`, `@chatgptricks`, `@kayo`).

This plan was adapted from an earlier TikTok version of the same exercise
(see `workflows/tiktok_growth_pipeline.md`) — TikTok work is paused because
its Content Posting API forces all unaudited posts to private for 2-4 weeks.
Instagram has a similar app-review gate but no forced-private period, so
this pipeline proceeds on Instagram first.

If the niche or pillars change, update the Google Doc first, then update
this section to point at the new source of truth.

## Content pillars (rotate across the week)
1. **AI Reimagines [Era/Genre]** — Reel cutdowns of the original AI-music
   format locked for the YouTube channel
   (`../Youtube Content Agent/workflows/daily_script_pipeline.md`), captioned
   in the long narrative style @evolving.ai uses
2. **AI Pop-Culture Reimagining** — anime/movie/game moments remade with AI
   video, emoji hook + branded follow-CTA (@airesearches style)
3. **AI Hip-Hop/Influencer Content** — AI-generated rap/performance content
   with a consistent persona, comment-to-DM lead magnet (@mrbankzzzz style)
4. **Tool-Drop Reactive Content** — same-day Reels riding newly launched AI
   video tools/models (@kayo style) — requires watching AI tool release news
5. **AI Dance/Character** — a recurring AI-generated persona in dance or
   crossover content, cross-postable with any future TikTok relaunch

## Cadence
1 Reel per day minimum (solo capacity). Stories are for retention with
existing followers, not discovery — don't count them toward the daily
posting goal. Stretch: attempt an Instagram Collab with another small
AI-content creator when the opportunity arises (publishes to both
audiences at once).

## Caption rules (the biggest platform difference vs. TikTok)
Unlike TikTok's minimal-caption style, long narrative captions (3-5
sentences of story/context) consistently outperform on this niche —
every top post studied writes like film criticism, not a hashtag stack.
Close every caption with an engagement question, and bake a follow-CTA
into the caption itself, not just the bio.

## Copyright / likeness guardrail
Same rule as the YouTube and TikTok pipelines: reimagine a style/era,
never a specific existing song or a specific living artist's likeness,
without legal sign-off. Applies most to Pillar 3.

## Inputs / tools
- `mcp__sandcastles__discover_channels`, `search_all_videos`,
  `channel_recap` — competitive research (already run once for this
  analysis; re-run periodically to catch new trends/creators)
- `mcp__sandcastles__get_personal_analytics` — @the_shedstudio is now
  watchlisted (added via `add_channels_to_watchlist` on 2026-08-10), so
  this becomes the primary tool for tracking real progress against the
  week-by-week milestones once content is posted
- `tools/create_google_doc.py` — deliverable output (OAuth via
  `tools/google_auth.py`, credentials copied from Youtube Content Agent
  on 2026-08-10)

## Posting (currently manual)
No Instagram upload/scheduling tool exists yet. Publishing is manual until
the Content Publishing API path below is built out.

**Requirements to automate:**
1. Instagram Business/Creator account linked to a Facebook Page — already
   satisfied, @the_shedstudio is a Business account ("The Shed Studio LLC")
2. A Meta app requesting `instagram_basic` and `instagram_content_publish`
   permissions
3. Meta App Review (2-4 weeks) for production access beyond 25 test users
4. Once approved: publishing is a two-step Graph API call — POST a media
   container to `/{ig-user-id}/media`, then publish via
   `/{ig-user-id}/media_publish`. Limits: 25 published posts/24hr (Reels
   and Stories share the bucket), 200 calls/user/hour.

This is less restrictive than TikTok's forced-`SELF_ONLY` pre-audit period,
but still an external dependency on completing Meta's app review before
`tools/post_to_instagram.py` can be built and tested end-to-end.

## Edge cases / things learned
- `channel_recap` on a bare handle (e.g. `the_shedstudio`) can fail with
  `channel_not_found` even for a real, existing account if Sandcastles
  hasn't indexed it yet. Use `add_channels_to_watchlist` with a full URL
  (`https://www.instagram.com/<handle>`) to submit it for scraping — a
  bare handle string was rejected as `invalid_input`, the full URL worked.
- Scraping a newly submitted channel takes a few minutes before
  `channel_recap`/`get_personal_analytics` return real data.
- On this niche, Instagram and TikTok favor opposite caption styles:
  TikTok rewards minimal hashtag-only captions, Instagram rewards long
  narrative captions. Don't reuse TikTok captions verbatim if TikTok work
  resumes later.
