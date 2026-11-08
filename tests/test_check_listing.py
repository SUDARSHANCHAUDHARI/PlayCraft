import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_listing as cl  # noqa: E402

GOOD = """TITLE: TrailMap: Offline Hiking
SHORT DESC: Find nearby trails and keep your route when you lose signal.
FULL DESC:
TrailMap shows trails near you.

WHY HIKERS USE TRAILMAP:
• Offline maps
• GPS track recording

CHARACTER COUNTS:
Title: 25/30
"""


def results(text):
    return {name: (ok, detail) for name, ok, detail in cl.check(cl.parse(text)[0])}


class Parse(unittest.TestCase):
    def test_single_block_fields(self):
        b = cl.parse(GOOD)[0]
        self.assertEqual(b["title"], "TrailMap: Offline Hiking")
        self.assertTrue(b["full"].startswith("TrailMap shows trails near you."))
        self.assertTrue(b["full"].endswith("• GPS track recording"))
        self.assertNotIn("CHARACTER COUNTS", b["full"])

    def test_multiple_locale_blocks(self):
        text = "LOCALE: th (Thai)\nTITLE: ก\nSHORT DESC: ข\nFULL DESC:\nค\nNOTES:\nNone\n" \
               "LOCALE: ja (Japanese)\nTITLE: あ\nSHORT DESC: い\nFULL DESC:\nう\n"
        blocks = cl.parse(text)
        self.assertEqual([b["locale"] for b in blocks], ["th", "ja"])
        self.assertEqual([b["full"] for b in blocks], ["ค", "う"])

    def test_two_blocks_without_locale_lines(self):
        self.assertEqual(len(cl.parse(GOOD + "\n" + GOOD)), 2)


class Checks(unittest.TestCase):
    def test_good_listing_passes_everything(self):
        self.assertTrue(all(ok for ok, _ in results(GOOD).values()), results(GOOD))

    def test_exact_lengths_at_and_over_the_limit(self):
        at = GOOD.replace("TrailMap: Offline Hiking", "x" * 30)
        over = GOOD.replace("TrailMap: Offline Hiking", "x" * 31)
        self.assertEqual(results(at)["Title length"], (True, "30/30"))
        self.assertEqual(results(over)["Title length"], (False, "31/30"))

    def test_cjk_counted_as_characters(self):
        text = "LOCALE: ja\nTITLE: " + "地" * 30 + "\nSHORT DESC: a\nFULL DESC:\nb\n"
        self.assertEqual(results(text)["Title length"], (True, "30/30"))

    def test_rules(self):
        bad = GOOD.replace("Find nearby trails", "The best and easy way. Download now. #1 app to find trails") \
                  .replace("TrailMap: Offline Hiking", "TrailMap 🏔 HIKING")
        r = results(bad)
        self.assertEqual(r["Banned words"], (False, "best, easy"))
        self.assertFalse(r["Superlative claims"][0])
        self.assertFalse(r["Call-to-action phrases"][0])
        self.assertFalse(r["Emoji in title"][0])
        self.assertEqual(r["ALL CAPS in title/short"], (False, "HIKING"))

    def test_acronyms_and_section_headers_allowed(self):
        r = results(GOOD.replace("Find nearby", "GPS and Find nearby"))
        self.assertTrue(r["ALL CAPS in title/short"][0])  # GPS is an acronym; header lines live in full desc

    def test_banned_words_only_for_english(self):
        text = "LOCALE: de\nTITLE: Best\nSHORT DESC: easy\nFULL DESC:\nx\n"
        self.assertNotIn("Banned words", results(text))

    def test_missing_field_fails(self):
        r = results("TITLE: Only a title\n")
        self.assertEqual(r["Short desc present"], (False, "missing"))


class Main(unittest.TestCase):
    def run_main(self, text):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
            f.write(text)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = cl.main([f.name])
        Path(f.name).unlink()
        return code, buf.getvalue()

    def test_exit_codes(self):
        self.assertEqual(self.run_main(GOOD)[0], 0)
        code, out = self.run_main(GOOD.replace("Find nearby", "best way to find"))
        self.assertEqual(code, 1)
        self.assertIn("FAIL  Banned words: best", out)
        self.assertEqual(self.run_main("nothing here")[0], 2)
        self.assertEqual(cl.main(["/nope/file.txt"]), 2)


if __name__ == "__main__":
    unittest.main()
