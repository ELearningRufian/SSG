import unittest

from textnode import *
from inlineutils import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        nodes = [TextNode("test text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("test text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_single_delimiter(self):
        nodes = [TextNode("test `code` text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [TextNode("test ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        nodes = [TextNode("test *italic* and *bold* text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("test ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold", TextType.ITALIC), # it says bold but the actual markdown is italic :P
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    #def test_nested_delimiters(self):
    #    nodes = [TextNode("test *italic and **bold** text* example", TextType.TEXT)]
    #    expected = [
    #        TextNode("test ", TextType.TEXT),
    #        TextNode("italic and **bold** text", TextType.ITALIC),
    #        TextNode(" example", TextType.TEXT)
    #    ]
    #    self.assertEqual(split_nodes_delimiter(nodes, "*", TextType.ITALIC), expected)

    def test_unbalanced_delimiters(self):
        nodes = [TextNode("test *italic text", TextType.TEXT)]
        with self.assertRaises(SyntaxError) as context:
            split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        result = str(context.exception)
        expected = "Invalid markdown. Missing closing delimiter in 'test *italic text'"
        self.assertEqual(result, expected)

    def test_mixed_delimiters(self):
        nodes = [TextNode("test *italic* and **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("test *italic* and ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_multiple_nodes(self):
        nodes = [TextNode("test *ital* text",TextType.TEXT), TextNode("foo *bar* baz *foobar*",TextType.TEXT)]
        result = split_nodes_delimiter(nodes,"*", TextType.ITALIC)
        expected = [
            TextNode("test ", TextType.TEXT, None), 
            TextNode("ital", TextType.ITALIC, None), 
            TextNode(" text", TextType.TEXT, None), 
            TextNode("foo ", TextType.TEXT, None), 
            TextNode("bar", TextType.ITALIC, None), 
            TextNode(" baz ", TextType.TEXT, None), 
            TextNode("foobar", TextType.ITALIC, None), 
            TextNode("", TextType.TEXT, None)
        ]
        self.assertEqual(result, expected)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "Here is an image: ![alt text](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        text = "Here are two images: ![first image](https://example.com/first.png) and ![second image](https://example.com/second.png)"
        result = extract_markdown_images(text)
        expected = [("first image", "https://example.com/first.png"), ("second image", "https://example.com/second.png")]
        self.assertEqual(result, expected)

    def test_no_images(self):
        text = "This text contains no images."
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_images_with_special_characters(self):
        text = "Image with special characters: ![alt @text](https://example.com/image@.png)"
        result = extract_markdown_images(text)
        expected = [("alt @text", "https://example.com/image@.png")]
        self.assertEqual(result, expected)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "Here is a [link](https://example.com)."
        result = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = "Here are two links: [first link](https://example1.com) and [second link](https://example2.com)."
        result = extract_markdown_links(text)
        expected = [("first link", "https://example1.com"), ("second link", "https://example2.com")]
        self.assertEqual(result, expected)

    def test_no_links(self):
        text = "This text contains no links."
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_links_with_special_characters(self):
        text = "Link with special characters: [link @text](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("link @text", "https://example.com")]
        self.assertEqual(result, expected)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        nodes = [TextNode("test text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [TextNode("test text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_single_delimiter(self):
        nodes = [TextNode("test `code` text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [TextNode("test ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        nodes = [TextNode("test *italic* and *bold* text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("test ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold", TextType.ITALIC), # it says bold but the actual markdown is italic :P
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    #def test_nested_delimiters(self):
    #    nodes = [TextNode("test *italic and **bold** text* example", TextType.TEXT)]
    #    expected = [
    #        TextNode("test ", TextType.TEXT),
    #        TextNode("italic and **bold** text", TextType.ITALIC),
    #        TextNode(" example", TextType.TEXT)
    #    ]
    #    self.assertEqual(split_nodes_delimiter(nodes, "*", TextType.ITALIC), expected)

    def test_unbalanced_delimiters(self):
        nodes = [TextNode("test *italic text", TextType.TEXT)]
        with self.assertRaises(SyntaxError) as context:
            split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        result = str(context.exception)
        expected = "Invalid markdown. Missing closing delimiter in 'test *italic text'"
        self.assertEqual(result, expected)

    def test_mixed_delimiters(self):
        nodes = [TextNode("test *italic* and **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("test *italic* and ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_multiple_nodes(self):
        nodes = [TextNode("test *ital* text",TextType.TEXT), TextNode("foo *bar* baz *foobar*",TextType.TEXT)]
        result = split_nodes_delimiter(nodes,"*", TextType.ITALIC)
        expected = [
            TextNode("test ", TextType.TEXT, None), 
            TextNode("ital", TextType.ITALIC, None), 
            TextNode(" text", TextType.TEXT, None), 
            TextNode("foo ", TextType.TEXT, None), 
            TextNode("bar", TextType.ITALIC, None), 
            TextNode(" baz ", TextType.TEXT, None), 
            TextNode("foobar", TextType.ITALIC, None), 
            TextNode("", TextType.TEXT, None)
        ]
        self.assertEqual(result, expected)

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_simple(self):
        node = TextNode("This is text with an image ![alt text](https://example.com/image.png) and more text", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and more text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple(self):
        node = TextNode("Text with ![image one](https://example.com/one.png) and ![image two](https://example.com/two.png)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("image one", TextType.IMAGE, "https://example.com/one.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image two", TextType.IMAGE, "https://example.com/two.png")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text without images", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [node]
        self.assertEqual(result, expected)

    def test_split_nodes_image_edge_case(self):
        node = TextNode("Edge case with image at end ![alt](https://example.com/image.png)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("Edge case with image at end ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/image.png")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_list(self):
        nodes = [
            TextNode("This is text with an image ![alt text](https://example.com/image.png) and more text", TextType.TEXT),
            TextNode("Text with ![image one](https://example.com/one.png) and ![image two](https://example.com/two.png)", TextType.TEXT)
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and more text", TextType.TEXT),
            TextNode("Text with ", TextType.TEXT),
            TextNode("image one", TextType.IMAGE, "https://example.com/one.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("image two", TextType.IMAGE, "https://example.com/two.png")
        ]
        self.assertEqual(result, expected)

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_single(self):
        node = TextNode("Links: [Google](https://google.com) and more text", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("Links: ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" and more text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [node]
        self.assertEqual(result, expected)

    def test_split_nodes_link_edge_case(self):
        node = TextNode("[Link](https://example.com) at start.", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("Link", TextType.LINK, "https://example.com"),
            TextNode(" at start.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_nodelist(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
            TextNode("Links: [Google](https://google.com) and more text", TextType.TEXT)
        ]
        result = split_nodes_link(nodes)
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode("Links: ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" and more text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

class testTextToTextnodes(unittest.TestCase):
    def test_text_to_text_nodes_allsix(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()