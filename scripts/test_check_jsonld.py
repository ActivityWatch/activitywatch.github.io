import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "check_jsonld", Path(__file__).with_name("check_jsonld.py")
)
check_jsonld = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_jsonld)


def page(block: str) -> str:
    return f'<html><script type="application/ld+json">{block}</script></html>'


class CheckHtmlTests(unittest.TestCase):
    def test_valid_block_passes(self):
        self.assertEqual(check_jsonld.check_html(page('{"@type": "WebSite"}')), [])

    def test_unparseable_block_fails(self):
        self.assertEqual(len(check_jsonld.check_html(page('{"a": "x\ny"}'))), 1)

    def test_non_json_constants_fail(self):
        for const in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(const=const):
                errors = check_jsonld.check_html(page(f'{{"ratingValue": {const}}}'))
                self.assertEqual(len(errors), 1)
                self.assertIn(const, errors[0])


if __name__ == "__main__":
    unittest.main()
