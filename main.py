"""One-line patch note for make.fun — Fix Human Sleep: Funniest Patch Note.

Writes exactly one line (1-160 chars) to /output/entry.txt.

Judge criteria, in order:
1. Reads as a real patch note announcing a fix for human sleep.
2. Funny: the joke lands on a single read and earns a laugh.
3. Sounds like genuine release notes: terse, confident, changelog voice.
4. Stays a single line under the cap, no padding or trailing explanation.
5. Surprises: the fix is specific and unexpected, not a flat claim.

Pattern: ONE concrete scene (sleep installs overnight) + ONE reversal
(eight hours of buffering replaced by an install) + ONE landing final line
(side effects include dreaming in 4K).
"""

import os

ENTRY = "Fixed: human sleep now installs overnight instead of eight hours of buffering; side effects include dreaming in 4K."
MAX_CHARS = 160


def validate(text):
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds 160 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(c) < 0x20 for c in text):
        raise SystemExit("entry contains a control character")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
