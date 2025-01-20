import unittest

from nodeutils import *
from htmlnode import HTMLNode
from textnode import TextNode

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_text_to_html_node(self):
        node = TextNode("test text", TextType.TEXT)
        result = text_node_to_html_node(node)
        expected = HTMLNode(tag=None, value="test text", children=None, props=None)
        self.assertEqual(result, expected)
        
    def test_text_node_bold_to_html_node(self):
        node = TextNode("test text", TextType.BOLD)
        result = text_node_to_html_node(node)
        expected = HTMLNode(tag="b", value="test text", children=None, props=None)
        self.assertEqual(result, expected)

    def test_text_node_italic_to_html_node(self):
        node = TextNode("test text", TextType.ITALIC)
        result = text_node_to_html_node(node)
        expected = HTMLNode(tag="i", value="test text", children=None, props=None)
        self.assertEqual(result, expected)

    def test_text_node_code_to_html_node(self):
        node = TextNode("test text", TextType.CODE)
        result = text_node_to_html_node(node)
        expected = HTMLNode(tag="code", value="test text", children=None, props=None)
        self.assertEqual(result, expected)

    def test_text_node_link_to_html_node(self):
        node = TextNode("test text", TextType.LINK, "https://testurl")
        result = text_node_to_html_node(node)
        expected = HTMLNode(tag="a", value="test text", children=None, props={'href': 'https://testurl'})
        self.assertEqual(result, expected)

    def test_text_node_image_to_html_node(self):
        node = TextNode("test text", TextType.IMAGE, "https://testurl")
        result = text_node_to_html_node(node)
        expected = HTMLNode(tag="img", value=None, children=None, props={'src': 'https://testurl', 'alt': 'test text'})
        self.assertEqual(result, expected)
    
if __name__ == "__main__":
    unittest.main()