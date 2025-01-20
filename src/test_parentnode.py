import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_flat(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        result = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(result, expected)

    def test_missing_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, [LeafNode("b", "Bold text")])
            node.to_html()
        result = str(context.exception)
        expected = 'Missing tag: HTMLNode(tag=None, value=None, children=[HTMLNode(tag="b", value="Bold text", children=None, props=None)], props=None)'
        self.assertEqual(result, expected)

    def test_missing_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("p", None)
            node.to_html()
        result = str(context.exception)
        expected = 'Missing children: HTMLNode(tag="p", value=None, children=None, props=None)'
        self.assertEqual(result, expected)

    def test_nested_children(self):
        node = ParentNode("div", [
            LeafNode("h1", "Heading"),
            ParentNode("ul", [
                LeafNode("li", "Item 1"),
                LeafNode("li", "Item 2")
            ])
        ])
        result = node.to_html()
        expected = "<div><h1>Heading</h1><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
