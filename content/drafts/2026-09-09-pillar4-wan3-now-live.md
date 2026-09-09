# 2026-09-09 — Pillar 4: Tool-Drop Reactive Content

**Title:** The 30-Second AI Video Tool We Faked Two Weeks Ago Just Went Real

**Hook (first 1-2 seconds):** Cold open on a single unbroken 30-second shot — a character walks from a rain-soaked street into a sunlit café, no cuts, no stitching, lighting and shadows staying locked to the same subject the entire time — text overlay: "we couldn't do this on 8/30. today we can."

**Caption:**
Two weeks ago we reacted to Wan 3.0 as a rumor — it wasn't in our tool stack yet, so we faked the capability with a dramatized reenactment and said so honestly in the caption. Today it's real: Wan 3.0 just landed in our stack, native 30-second single-pass clips with no stitching, meaning a subject can walk street to café to skyline and never once glitch or reset. We rebuilt the exact same shot from that earlier post, this time for real, so you can see what "the tool finally showing up" actually looks like next to what we guessed it would look like. We'd rather admit when we're reenacting a capability than pretend a mockup is the real thing — that's the whole point of this series. Could you tell which half of this pair was the real render and which was the guess? Follow @the_shedstudio — we react to every drop the week it's actually usable, not just announced.

**Production Notes:**
Reactive/tool-drop piece confirming Wan 3.0 (`wan3-0`) is now live in `openart_model_list` as of 2026-09-09 — it was NOT present in the 2026-08-25 or 2026-08-30 catalog checks logged in this workflow's edge-case log, where the 08-30 Pillar 4 draft had to fall back to a dramatized Kling 3 Omni reenactment because the real model wasn't available yet. This draft closes that loop with a literal render on the now-available model: single continuous take (street → café), text2video from a detailed prompt, standard tier (30s single-pass is the whole hook, no need for the 1.75x "prime" tier here). No existing franchise/likeness used — original character, satisfies the copyright/likeness guardrail.

**Model:** Wan 3.0 (text2video, `mode: "standard"`, native audio track)

**Status:** Pending — awaiting human approval in the Autosheet content sheet before rendering. Could not be appended to the sheet this run: Autosheet is still blocked by the `api-billing-free-trial-ended` outage (11th consecutive day as of 2026-09-09) — needs manual entry once billing is resolved.
