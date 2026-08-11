"""Generate an original AI song via the Apiframe v2 Suno API.

Third-party Suno wrapper (Suno itself has no public API as of 2026-08).
Uses APIFRAME_API_KEY from .env. API key prefix 'afk_' = Apiframe v2 -
use api.apiframe.ai/v2, NOT the older api.apiframe.pro v1 endpoints
(v1 endpoints return a 400 telling you this if you get it wrong).

Usage as a library:
  from generate_music import generate_song
  audio_url = generate_song(title="...", style="...", prompt="...")

Usage as a script:
  .venv/bin/python tools/generate_music.py "Title" "style/tags" "prompt text"
"""

import os
import sys
import time

import requests
from dotenv import load_dotenv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT, ".env"))

API_BASE = "https://api.apiframe.ai/v2"
API_KEY = os.environ.get("APIFRAME_API_KEY")

POLL_INTERVAL_SECONDS = 10
MAX_POLL_ATTEMPTS = 60  # 10 minutes


def _headers():
    if not API_KEY:
        raise SystemExit("FAIL: APIFRAME_API_KEY not set in .env")
    return {"Content-Type": "application/json", "X-API-Key": API_KEY}


def generate_song(title, style, prompt, instrumental=False, model_version="V4_5PLUS"):
    """Submit a song generation job and poll until it finishes.

    `prompt` describes the song for Suno to write; for full custom lyrics
    instead, pass custom_mode=True and put the lyrics in `prompt` with
    [Verse]/[Chorus] section markers (not yet exposed as a separate arg
    here - add if a pillar needs it). Returns the first track's audio URL.
    """
    body = {
        "prompt": prompt,
        "model": "suno",
        "sunoParams": {
            "model_version": model_version,
            "style": style,
            "custom_mode": False,
            "title": title,
            "instrumental": instrumental,
        },
    }

    resp = requests.post(f"{API_BASE}/music/generate", json=body, headers=_headers())
    resp.raise_for_status()
    job_id = resp.json()["jobId"]

    for _ in range(MAX_POLL_ATTEMPTS):
        time.sleep(POLL_INTERVAL_SECONDS)
        status_resp = requests.get(f"{API_BASE}/jobs/{job_id}", headers=_headers())
        status_resp.raise_for_status()
        result = status_resp.json()
        status = result.get("status")
        if status == "COMPLETED":
            tracks = result.get("result", {}).get("tracks") or []
            if not tracks:
                raise SystemExit(f"FAIL: job {job_id} completed with no tracks: {result}")
            return tracks[0]["audioUrl"]
        if status in ("FAILED", "ERROR"):
            raise SystemExit(f"FAIL: job {job_id} failed: {result}")
        # QUEUED / PROCESSING - keep polling

    raise SystemExit(f"FAIL: job {job_id} did not finish within {MAX_POLL_ATTEMPTS * POLL_INTERVAL_SECONDS}s")


def main():
    if len(sys.argv) != 4:
        sys.exit('Usage: generate_music.py "Title" "style/tags" "prompt text"')
    title, style, prompt = sys.argv[1], sys.argv[2], sys.argv[3]
    url = generate_song(title=title, style=style, prompt=prompt)
    print(url)


if __name__ == "__main__":
    main()
