import unittest

from websiteutils import *

class TestWebsiteUtils(unittest.TestCase):
    def test_extract_title_happycase(self):
        text = "This is my website\n\n# SSG Sample Website\n\nContent goes here"
        result = extract_title(text)
        expected = "SSG Sample Website"
        self.assertEqual(result, expected)

    def test_extract_title_notpresent(self):
        text = "This is my website\n\n## SSG Sample Website\n\nContent goes here"
        with self.assertRaises(Exception) as context:
            extract_title(text)
        result = str(context.exception)
        expected = 'Page Title (h1) not found'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()