import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="img", props={"src":"someimg.jpg", "alt":"somealttext", "width":"0", "height":"0"})
        result = node.props_to_html()
        expected = ' src="someimg.jpg" alt="somealttext" width="0" height="0"'
        self.assertEqual(result, expected)

    def test_props_to_html_noprops(self):
        node = HTMLNode(tag="img")
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)

    def test_repr_value(self):
        node = HTMLNode(tag="h1", value="This is a title")
        result = str(node)
        expected = 'HTMLNode(tag="h1", value="This is a title", children=None, props=None)'
        self.assertEqual(result, expected)

    def test_repr_children(self):
        child1 = HTMLNode(tag="h1", value="This is a title")
        child2 = HTMLNode(tag="h2", value="This is a smaller title")
        node = HTMLNode(tag="header", children=[child1, child2])
        result = str(node)
        expected = 'HTMLNode(tag="header", value=None, children=[HTMLNode(tag="h1", value="This is a title", children=None, props=None), HTMLNode(tag="h2", value="This is a smaller title", children=None, props=None)], props=None)'
        self.assertEqual(result, expected)

    def test_repr_props(self):
        node = HTMLNode(tag="img", props={"src":"someimg.jpg", "alt":"somealttext", "width":"0", "height":"0"})
        result = str(node)
        expected = "HTMLNode(tag=\"img\", value=None, children=None, props={'src': 'someimg.jpg', 'alt': 'somealttext', 'width': '0', 'height': '0'})"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()