"""Create a Google Doc from structured content and share the link.

Takes a title and a list of content blocks (headings + paragraphs + bullet
lists) and writes them into a new Google Doc via the Docs API, using the
OAuth credentials already set up for this project (credentials.json ->
token.json, same flow as verify_setup.py).

Block format (list of dicts), e.g.:
  [
    {"type": "h1", "text": "My Title"},
    {"type": "h2", "text": "Section"},
    {"type": "p", "text": "Some paragraph."},
    {"type": "bullet", "text": "A bullet point"},
  ]

Usage as a library:
  from create_google_doc import create_doc
  url = create_doc("Doc Title", blocks)

Usage as a script (reads blocks JSON from a file):
  .venv/bin/python tools/create_google_doc.py "Doc Title" path/to/blocks.json
"""

import json
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_auth import get_credentials

HEADING_STYLE = {
    "h1": "HEADING_1",
    "h2": "HEADING_2",
    "h3": "HEADING_3",
}


def create_doc(title, blocks):
    creds = get_credentials()
    docs = build("docs", "v1", credentials=creds)

    doc = docs.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]

    # A single batchUpdate applies requests in order against the document
    # state produced by prior requests in the same batch, so inserting each
    # block's text at a cumulatively-advancing index keeps offsets correct.
    requests = []
    index = 1
    style_ranges = []
    for block in blocks:
        text = block["text"].rstrip("\n") + "\n"
        requests.append({"insertText": {"location": {"index": index}, "text": text}})
        style_ranges.append((index, index + len(text), block["type"]))
        index += len(text)

    for start, end, btype in style_ranges:
        if btype in HEADING_STYLE:
            requests.append({
                "updateParagraphStyle": {
                    "range": {"startIndex": start, "endIndex": end},
                    "paragraphStyle": {"namedStyleType": HEADING_STYLE[btype]},
                    "fields": "namedStyleType",
                }
            })
        elif btype == "bullet":
            requests.append({
                "createParagraphBullets": {
                    "range": {"startIndex": start, "endIndex": end},
                    "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                }
            })

    try:
        docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
    except HttpError as e:
        sys.exit(f"FAIL: Docs batchUpdate failed: {e}")

    return f"https://docs.google.com/document/d/{doc_id}/edit"


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: create_google_doc.py <title> <blocks.json>")
    title = sys.argv[1]
    with open(sys.argv[2]) as f:
        blocks = json.load(f)
    url = create_doc(title, blocks)
    print(url)


if __name__ == "__main__":
    main()
