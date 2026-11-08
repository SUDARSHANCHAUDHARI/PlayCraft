#!/usr/bin/env python3
"""Deterministic checks on Play Store listing blocks: exact character counts and the fixed rules.

Reads the PlayCraft output format, one or more blocks:

    LOCALE: th            (optional; absent means the default-locale listing)
    TITLE: ...
    SHORT DESC: ...
    FULL DESC:
    ...                   (until CHARACTER COUNTS:, NOTES:, the next LOCALE: or end of file)

Prints one report per block and exits 1 if any block fails, 0 if all pass, 2 on unreadable input.
Characters are counted as Unicode code points.

usage: check_listing.py <file>   (or - for stdin)
"""
import re
import sys
import unicodedata
from pathlib import Path

LIMITS = {"title": 30, "short": 80, "full": 4000}
BANNED_EN = ("easy", "simple", "best", "amazing", "powerful")
SUPERLATIVES = (r"#\s?1\b", r"\bnumber one\b", r"\bworld'?s best\b", r"\bmost downloaded\b", r"\btop rated\b")
CTA = (r"\bdownload now\b", r"\binstall now\b", r"\bget it now\b")
ACRONYM_OK = {"GPS", "PDF", "QR", "USB", "AI", "VPN", "API", "SMS", "NFC", "HD", "UI", "OCR", "AR", "VR"}


def parse(text):
    """List of dicts with locale, title, short, full."""
    blocks, cur, field = [], None, None
    for line in text.splitlines():
        m = re.match(r"\s*(LOCALE|TITLE|SHORT DESC|FULL DESC|CHARACTER COUNTS|NOTES):\s?(.*)$", line)
        if m:
            key, rest = m.group(1), m.group(2)
            if key == "LOCALE" or (key == "TITLE" and cur and cur.get("title") is not None):
                cur = {"locale": rest.split()[0] if key == "LOCALE" and rest else None,
                       "title": None, "short": None, "full": None}
                blocks.append(cur)
                field = None
                if key == "LOCALE":
                    continue
            if cur is None:
                cur = {"locale": None, "title": None, "short": None, "full": None}
                blocks.append(cur)
            if key == "TITLE":
                cur["title"], field = rest.strip(), None
            elif key == "SHORT DESC":
                cur["short"], field = rest.strip(), None
            elif key == "FULL DESC":
                cur["full"], field = rest, "full"
            else:
                field = None
            continue
        if field == "full":
            cur["full"] = (cur["full"] + "\n" + line) if cur["full"] else line
    for b in blocks:
        if b["full"] is not None:
            b["full"] = b["full"].strip("\n")
    return [b for b in blocks if b["title"] is not None or b["short"] is not None or b["full"] is not None]


def has_emoji(s):
    return any(unicodedata.category(ch) == "So" or 0x1F000 <= ord(ch) <= 0x1FAFF for ch in s)


def caps_words(s):
    return [w for w in re.findall(r"\b[A-Z]{4,}\b", s) if w not in ACRONYM_OK]


def check(block):
    """List of (check name, ok, detail)."""
    out = []
    english = (block["locale"] or "en").lower().startswith("en")
    for key, name in (("title", "Title"), ("short", "Short desc"), ("full", "Full desc")):
        value = block[key]
        if value is None:
            out.append((f"{name} present", False, "missing"))
            continue
        n = len(value)
        out.append((f"{name} length", n <= LIMITS[key], f"{n}/{LIMITS[key]}"))
    every = "\n".join(v for v in (block["title"], block["short"], block["full"]) if v)
    if english:
        hits = sorted({w.lower() for w in re.findall(r"\b(" + "|".join(BANNED_EN) + r")\b", every, re.I)})
        out.append(("Banned words", not hits, ", ".join(hits) or "none"))
    sup = [p for p in SUPERLATIVES if re.search(p, every, re.I)]
    out.append(("Superlative claims", not sup, ", ".join(re.sub(r"\\b|\\s\?|'\?", "", p) for p in sup) or "none"))
    cta = [p for p in CTA if re.search(p, every, re.I)]
    out.append(("Call-to-action phrases", not cta, ", ".join(p.replace("\\b", "") for p in cta) or "none"))
    title = block["title"] or ""
    out.append(("Emoji in title", not has_emoji(title), "found" if has_emoji(title) else "none"))
    caps = caps_words(f"{title} {block['short'] or ''}")
    out.append(("ALL CAPS in title/short", not caps, ", ".join(caps) or "none"))
    return out


def report(block, results):
    label = block["locale"] or "default locale"
    lines = [f"LISTING CHECK — {label}"]
    lines += [f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}" for name, ok, detail in results]
    lines.append(f"  {sum(ok for _, ok, _ in results)} of {len(results)} checks pass")
    return "\n".join(lines)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 2
    try:
        text = sys.stdin.read() if argv[0] == "-" else Path(argv[0]).read_text(encoding="utf-8")
    except OSError as e:
        print(f"cannot read {argv[0]}: {e}", file=sys.stderr)
        return 2
    blocks = parse(text)
    if not blocks:
        print("no listing blocks found (expected TITLE:, SHORT DESC:, FULL DESC:)", file=sys.stderr)
        return 2
    failed = False
    for b in blocks:
        results = check(b)
        failed |= not all(ok for _, ok, _ in results)
        print(report(b, results))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
