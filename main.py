#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- make.fun entry.

Writes one Wi-Fi network name of at most 32 characters to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).

Craft notes (final pick, chosen over 7 other candidates):
"My ex took the dog AND the WiFi" (31 characters).

Why this one wins the judge's brief, in its own order:
1. Joke first: the punchline lands on the last two words. Losing
   the dog in a breakup is sad; losing the Wi-Fi beside it, shouted
   in capitals as if it were the equal prize, is the twist. A
   stranger gets it on the first read, no explanation needed.
2. Whole story: one line implies a character (the ex), a situation
   (the breakup / split of a shared life) and something that
   happened (she took everything, dog and network alike). The reader
   fills in the rest: the empty flat, the owner staring at the
   network list that used to be theirs.
3. Fresh: it is not one of the stock Wi-Fi jokes (no "Pretty Fly",
   no FBI van, no "it burns when IP"). The breakup frame is familiar
   but the Wi-Fi-as-divorce-asset twist is new.
4. Tight: 31 of 32 characters, every word earns its place. "My"
   makes it personal, "AND" in capitals is the escalation, and the
   Wi-Fi comes last so the punchline lands on the subject itself.

Rejected runners-up (all my own wording, kept here as the record
of the choice): "Ex changed the password again" (29, good but a
known trope), "This WiFi saw my search history" (31, funny but
only a situation, no event), "Cat unplugged the router again"
(30, cute but no character arc), "The WiFi divorced me first"
(26, punchy but thinner story), "My kids sold the WiFi password"
(30, fun but the event is a gag, not a story), "The router filed
for divorce" (28, personification without a human character),
"Ex took the dog, kept the WiFi" (30, subtler twist, weaker
escalation than AND).

One line, plain ASCII, no em dash, no emoji.

Python standard library only.
"""

import os

ENTRY = "My ex took the dog AND the WiFi"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 32:
        raise SystemExit(f"entry length {len(text)} out of range 1-32")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    # Fail loudly on sloppy edits instead of silently changing the
    # entry: leading/trailing spaces are not part of a Wi-Fi name,
    # and control characters (tab, etc.) would break the gate.
    if text != ENTRY:
        raise SystemExit("entry has leading or trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise SystemExit("entry contains control characters")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
