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

## Content approval sheet

The Autosheet 'Shed Studio - Instagram Content Approval' sheet (referenced
in the daily routine prompt) is this Google Sheet, business account
(`theshedstudio727@gmail.com`), tab `Content`:
https://docs.google.com/spreadsheets/d/1AaUO3Cj0Ypi0Ghbr6f1X1VxZwuceTn58vqBuRCAe8O8/edit

Columns: Date, Pillar, Title, Hook, Caption, Production Notes, Model,
Status, Video URL, Notes. Status flow: "Pending" (default, set when
drafting) → "Approved" (set by the human) → "Rendered" (set once rendered
and emailed for review). Created 2026-08-23 after two consecutive runs
(08-22, 08-23) failed at Part A with no spreadsheet ID stored anywhere
reachable — this line is now that source of truth. Update it here first
if the sheet is ever recreated.

## Content pillars (rotate across the week)
1. **AI Reimagines [Era/Genre]** — Reel cutdowns of the original AI-music
   format locked for the YouTube channel
   (`../Youtube Content Agent/workflows/daily_script_pipeline.md`), captioned
   in the long narrative style @evolving.ai uses. Model: PixVerse V6 for
   the visual (silent) + `tools/generate_music.py` for the song, combined
   in a video editor — see "Video model selection" below.
2. **AI Pop-Culture Reimagining** — anime/movie/game moments remade with AI
   video, emoji hook + branded follow-CTA (@airesearches style). Model:
   **Kling 3 Omni** (default as of 2026-08-11) — better physics/cinematic
   fidelity for era-mashup/epic content than PixVerse.
3. **AI Hip-Hop/Influencer Content** — AI-generated rap/performance content
   with a consistent persona, comment-to-DM lead magnet (@mrbankzzzz style).
   Model: Kling 3 Omni with `generateSound: true` when dialogue/vocals
   are needed.
4. **Tool-Drop Reactive Content** — same-day Reels riding newly launched AI
   video tools/models (@kayo style) — requires watching AI tool release news.
   Model: **Kling 3 Omni** (default as of 2026-08-11), same reasoning as
   Pillar 2.
5. **AI Dance/Character** — a recurring AI-generated persona in dance or
   crossover content, cross-postable with any future TikTok relaunch.
   Model: PixVerse V6 (cheap, fast, proven for stylized motion — no need
   for Kling's extra fidelity/cost/time here).

## Video model selection (updated 2026-08-11)
Researched the current AI video landscape for cheapest-vs-highest-quality
(see sources logged in conversation, not repeated here). Within OpenArt
(already a paid subscription, so this is a model choice, not a platform
migration):
- **PixVerse V6** — cheapest, fastest (~40-60s/clip), best for
  high-volume stylized/anime motion. Default for Pillars 3 (visual
  half) and 5.
- **Kling 3 Omni** — near-frontier quality (#4 on the Artificial
  Analysis ELO leaderboard), best-in-class physics for cinematic/epic
  content, noticeably slower (~2-3 min/clip in testing vs PixVerse's
  ~1 min) and pricier per clip. Default for Pillars 2 and 4.
- **Seedance 2.0** — highest raw quality/character-consistency (#1 ELO),
  reserve for cases where that specifically matters enough to justify
  the added cost/time over Kling.
- Considered switching to a cheaper aggregator (fal.ai) for the same
  underlying models instead of OpenArt's markup, but not worth it while
  the OpenArt subscription is already paid for — revisit if that
  changes.

## Daily trending songs (genre-mixed)
Replaces the one-time "growth strategy doc" step in the day-to-day
pipeline — instead of re-writing strategy daily, pull a fresh top-5
trending-songs snapshot each run for trend awareness. Pull from a public
chart (e.g. kworb.net's Spotify daily global chart) and select **one pick
per distinct genre lane**, not the raw top 5 — the raw top of most charts
skews heavily toward pop/mainstream, which biases every downstream
decision toward one genre if used as-is. Write the result to
`content/trending_audio/YYYY-MM-DD.md`.

This is trend-awareness input only, not a source of audio to embed
directly — the copyright/likeness guardrail still applies: never use a
specific existing song in generated content without legal sign-off. Use
it to judge which pillar/format is timely, not as a track to license or
rip.

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
- `tools/generate_music.py` — original AI song generation for Pillar 1,
  via the Apiframe v2 Suno wrapper (`APIFRAME_API_KEY` in `.env`). Suno
  itself has no public API as of 2026-08, this is a third-party wrapper.
  Use with `mcp__openart__openart_generate_video` (PixVerse V6, silent)
  for the visual half — combine the two in a standard video editor, see
  the "Edge cases" note below on why they can't be generated as one call.

## Posting (currently manual)
No Instagram upload/scheduling tool exists yet. Publishing is manual until
the Content Publishing API path below is built out.

**Requirements to automate:**
1. Instagram Business/Creator account linked to a Facebook Page — already
   satisfied, @the_shedstudio is a Business account ("The Shed Studio LLC")
2. A Meta app requesting `instagram_business_content_publish` (the current
   permission name - `instagram_content_publish` was the older name)
3. Meta App Review (2-4 weeks) for production access beyond 25 test users -
   **app created and submitted for review on 2026-08-11**, waiting on
   Meta's decision. Once an access token exists, build
   `tools/post_to_instagram.py` against step 4 below.
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
- 2026-08-11: `get_personal_analytics` for @the_shedstudio still returns
  `report_state: "initializing"` / "No verified channels yet" even though
  the channel is on the watchlist and `channel_recap` can already see it
  (71 followers). Being watchlisted isn't the same as being "verified" for
  personal analytics — there's a separate verification step not yet done.
- 2026-08-11 (correction, see below for what actually works): initially
  assumed Kling 3 Omni / Seedance 2.0's audio-element support could sync
  a full song to video in one call. It can't — that audio-element feature
  is for short 2-15s voice/dialogue clips (lip-sync), not a ~4-minute
  song bed. Kling 3 Omni's `visualReferences` doesn't even accept a
  generic audio type at all (only image/character/element refs with an
  optional short character *voice* clip). For Pillar 1: generate the song
  and the visual separately, combine in a standard video editor. PixVerse
  V6 (silent, text2video) is fine for the visual half after all.
- 2026-08-11: added `tools/generate_music.py` for Pillar 1's original
  songs, via Apiframe's v2 Suno API. Key detail: an API key starting
  with `afk_` is v2 — use `https://api.apiframe.ai/v2`, NOT the older
  `https://api.apiframe.pro` v1 endpoints (hitting v1 with a v2 key
  returns a 400 that helpfully names the correct base URL). v2 flow:
  `POST /v2/music/generate` with `{"prompt", "model": "suno",
  "sunoParams": {"model_version", "style", "custom_mode", "title",
  "instrumental"}}` → returns `jobId`; poll `GET /v2/jobs/{jobId}` until
  `status: "COMPLETED"`, audio URL at `result.tracks[0].audioUrl`. Suno
  itself still has no public API — this is a paid third-party wrapper.
- 2026-08-11: the cloud routine (`trig_0184eQthhejdSKjd6yboX5fz`) has been
  unreliable/opaque to debug — the RemoteTrigger API exposes zero run
  output/logs, only routine config. A full pipeline run and an isolated
  Autosheet-only smoke test both sat for 10-70+ minutes with no observable
  commit. OpenArt (`mcp__openart__*`) and Sandcastles were confirmed
  working when called directly/locally, so the cloud environment or the
  Autosheet connector specifically is the leading suspect — unconfirmed,
  since the claude.ai UI (the only place with real logs) wasn't checked
  during this session. This run was done manually/locally instead as a
  workaround; Autosheet and Gmail steps were skipped since those
  connectors aren't available outside the cloud routine.
