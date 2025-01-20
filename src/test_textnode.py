import unittest

from textnode import *
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_repr(self):
        result = str(TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev"))
        expected = 'TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()