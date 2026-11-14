"""Offline smoke tests for the Substack importer; no network or GitHub writes."""
import tempfile
from pathlib import Path
import unittest

from scripts import sync_substack as importer


def rss(body="Hello **world**", category="Català", title="Els nombres i l'amor"):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel><title>Converses de casa</title>
<item><title>{title.replace('&', '&amp;')}</title>
<link>https://gboschbo.substack.com/p/els-nombres-i-lamor</link>
<pubDate>Sat, 14 Nov 2026 08:00:00 +0100</pubDate>
<category>{category}</category>
<content:encoded><![CDATA[<p>{body}</p>]]></content:encoded>
</item></channel></rss>""".encode("utf-8")


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.original_posts = importer.POSTS
        self.original_translations = importer.TRANSLATIONS_FILE
        importer.POSTS = Path(self.tmp.name) / "_posts"
        importer.TRANSLATIONS_FILE = Path(self.tmp.name) / "translations.json"

    def tearDown(self):
        importer.POSTS = self.original_posts
        importer.TRANSLATIONS_FILE = self.original_translations
        self.tmp.cleanup()

    def test_create_update_and_idempotence(self):
        self.assertEqual(importer.sync(rss()), (1, 0))
        paths = list(importer.POSTS.glob("*.md"))
        self.assertEqual(len(paths), 1)
        first = paths[0].read_text()
        self.assertIn("categories: [personal]", first)
        self.assertIn("tags: [converses-de-casa]", first)
        self.assertIn("lang: ca", first)
        self.assertIn("Els nombres i l'amor", first)
        self.assertEqual(importer.sync(rss()), (0, 0))
        self.assertEqual(importer.sync(rss(body="Edited text")), (0, 1))
        self.assertIn("Edited text", paths[0].read_text())

    def test_explicit_language_tag(self):
        self.assertEqual(importer.sync(rss(category="English")), (1, 0))
        text = next(importer.POSTS.glob("*.md")).read_text()
        self.assertIn("lang: en", text)
        self.assertIn("permalink: /en/converses-de-casa/", text)

    def test_translation_grouping(self):
        import json
        importer.TRANSLATIONS_FILE.write_text(json.dumps({
            "numbers-and-love": [
                "https://gboschbo.substack.com/p/els-nombres-i-lamor",
                "https://gboschbo.substack.com/p/numbers-and-love"
            ]
        }), encoding="utf-8")
        self.assertEqual(importer.sync(rss()), (1, 0))
        text = next(importer.POSTS.glob("*.md")).read_text()
        self.assertIn('translation_key: "numbers-and-love"', text)
        self.assertEqual(importer.sync(rss()), (0, 0))

    def test_invalid_translation_mapping_fails_closed(self):
        importer.TRANSLATIONS_FILE.write_text('{"x": ["http://example.com/a"]}', encoding="utf-8")
        with self.assertRaises(ValueError):
            importer.sync(rss())

    def test_empty_feed_fails_closed(self):
        with self.assertRaises(ValueError):
            importer.sync(b"<rss><channel></channel></rss>")


if __name__ == "__main__":
    unittest.main()
