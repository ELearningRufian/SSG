import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_value(self):
        thrown = False
        node = LeafNode("img", None, props={"src":"someimg.jpg", "alt":"somealttext", "width":"0", "height":"0"})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        result = str(context.exception)
        expected = "Leaf node MUST have a value"
        self.assertEqual(result, expected)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is raw text")
        result = node.to_html()
        expected = "This is raw text"
        self.assertEqual(result, expected)

    def test_to_html_value(self):
        node = LeafNode("h1", "This is a header")
        result = node.to_html()
        expected = '<h1>This is a header</h1>'
        self.assertEqual(result, expected)


    def test_to_html_tag_and_props(self):
        node = LeafNode("a", "Visit boot.dev!", props={"href":"https://boot.dev"})
        result = node.to_html()
        expected = '<a href="https://boot.dev">Visit boot.dev!</a>'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()