# TikTok Growth Pipeline

## Objective
Grow the Shed Studio TikTok account from 0 followers toward a 10,000-follower
target within 30 days by publishing daily AI-generated short-form content
across 5 proven content pillars, and by tracking real performance data once
the account is live and verified in Sandcastles.

## Current strategy (locked 2026-08-10)
Full competitive research and the 30-day plan live in the Google Doc
**"TikTok Growth Plan: 0 to 10K in 30 Days"**:
https://docs.google.com/document/d/1tvoAUnzl80kyWV8MebAOFtlvyWeTrELLmvphuGrQE0k/edit

Niche: AI-generated viral videos — hip hop, anime, dance culture, pop
culture. Built from live TikTok creator/video data pulled via the
Sandcastles MCP server, studying 5 real accounts (`@p4pulya`, `@chibidoki`,
`@americanbaron`, `@sav.studies`, `@mrbankzzzz`).

If the niche or pillars change, update the Google Doc first, then update
this section to point at the new source of truth.

## Content pillars (rotate across the week)
1. **AI Reimagines [Era/Genre]** — short cutdowns of the same original
   AI-music format locked for the YouTube channel
   (`../Youtube Content Agent/workflows/daily_script_pipeline.md`)
2. **AI Anime Crossover** — hashtag-driven anime-style AI clips
3. **AI Dance/Character** — a recurring AI-generated persona
4. **AI Novelty Spike** — occasional wildcard "look what AI can do" post
5. **Trend/Ranking Commentary** — tightly on-topic AI/music/pop-culture
   reactions, "top 3" style

## Cadence
1 original post per day minimum (solo capacity). A second lighter-lift post
is a stretch goal, never at the cost of Pillar 1-3 quality. Test 2-3 posting
time slots in week 1 (6-10pm local audience time), lock in the best slot for
week 2 onward.

## Copyright / likeness guardrail
Same rule as the YouTube pipeline: reimagine a style/era, never a specific
existing song or a specific living artist's likeness, without legal
sign-off. This applies most to Pillar 5 (AI rap/deepfake-adjacent content).

## Inputs / tools
- `mcp__sandcastles__discover_channels`, `search_all_videos`,
  `channel_recap` — competitive research (already run once for the Phase 1
  analysis above; re-run periodically to catch new trends/creators)
- `mcp__sandcastles__get_personal_analytics` — **blocked until the TikTok
  channel is posted to and verified in Sandcastles.** Once available, this
  becomes the primary tool for tracking real progress against the
  week-by-week milestones in the plan doc.
- `tools/create_google_doc.py` — deliverable output, same pattern as the
  YouTube project (OAuth via `tools/google_auth.py`, credentials copied
  from Youtube Content Agent on 2026-08-10)

## Posting (currently manual)
No TikTok upload/scheduling tool exists yet. Publishing is manual until the
Content Posting API path below is built out.

**Why it's not automated yet:** TikTok requires an app to be registered on
the TikTok for Developers portal and to pass an audit (2-4 weeks, multiple
review rounds) before it can post anything publicly. An unaudited app can
only post as `SELF_ONLY` (private), capped at 5 users/24hrs — not usable for
real growth. Even post-audit, there's a shared ~15 posts/day/creator cap
across all API clients, and every post requires a non-preset user
confirmation screen (music usage, privacy, duet/comment settings).

**To unblock automation:**
1. Register an app at TikTok for Developers, add the Content Posting API
   product, request the `video.publish` scope
2. Submit for audit (TikTok will want a demo of the full flow — sandbox
   mode allows building/testing this pre-audit under `SELF_ONLY`)
3. Once audited: build `tools/tiktok_auth.py` (OAuth/Login Kit, mirroring
   `google_auth.py`'s pattern) and `tools/post_to_tiktok.py` (init → upload
   → status-check against `/v2/post/publish/video/init/`)

This is an external dependency on the user completing TikTok's developer
registration — not something that can be built and tested end-to-end until
app credentials exist.

## Edge cases / things learned
- Sandcastles' `get_personal_analytics` returns `report_state:
  "initializing"` with no data until a channel is verified — confirmed
  2026-08-10, the account had not posted yet.
- `discover_channels` without a TikTok-specific angle in the query returns
  mostly Instagram AI-tool-tutorial channels, not TikTok entertainment
  creators — narrow the query toward content *type* (e.g. "AI anime edit
  viral") rather than "AI tools" to surface the right niche.
- `channel_recap` needs a UUID (not just a handle) when a handle matches
  multiple platforms — check `discover_channels`/`search_all_videos`
  results for the UUID first, or expect an `ambiguous_channel` error with
  candidates to disambiguate from.
