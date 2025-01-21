import unittest

from blockutils import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_threeblocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        result = markdown_to_blocks(text)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(result, expected)
class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_h(self):
        text = ["# header"]
        expected = ["h1"]
        for i in range(1,6):
            text.append("#"+text[i-1])
            expected.append(f"h{i+1}")
        result = list(map(block_to_block_type, text))
        self.assertEqual(result, expected)

    def test_block_to_block_type_code(self):
        text = "```code line 1\ncode line 2\ncode line 3```"
        expected = "code"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_blockquote(self):
        text = ">quote line 1\n>quote line 2\n>quote line 3"
        expected = "blockquote"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_ul(self):
        text = "* list line 1\n- list line 2\n* list line 3"
        expected = "ul"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_ol(self):
        text = "1. list line 1\n2. list line 2\n3. list line 3"
        expected = "ol"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_h_bad(self):
        text = "####### header"
        expected = "p"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_code_bad(self):
        text = "```code line 1\ncode line 2```\ncode line 3``"
        expected = "p"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_blockquote_bad(self):
        text = ">quote line 1\nquote line 2\n>quote line 3"
        expected = "p"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_ul(self):
        text = "* list line 1\n-list line 2\n* list line 3"
        expected = "p"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

    def test_block_to_block_type_ul(self):
        text = "1. list line 1\n2.list line 2\n3. list line 3"
        expected = "p"
        result = block_to_block_type(text)
        self.assertEqual(result, expected)

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        text="some simple text"
        expected = ParentNode("div", [LeafNode("p", "some simple text")])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_paragraph(self):
        text="## header"
        expected = ParentNode("div", [ParentNode("h2", [LeafNode(None, "header")])])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_code(self):
        text = "```code line 1\ncode line 2\ncode line 3```"
        expected = ParentNode("div", [ParentNode("code", [LeafNode(None, "code line 1\ncode line 2\ncode line 3")])])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_blockquote(self):
        text = ">quote line 1\n>quote line 2\n>quote line 3"
        expected = ParentNode("div", [ParentNode("blockquote", [LeafNode(None, "quote line 1\nquote line 2\nquote line 3")])])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_ul(self):
        text = "* list line 1\n- list line 2\n* list line 3"
        expected = ParentNode("div", [ParentNode("ul", [ParentNode("li", [LeafNode(None, "list line 1")]), ParentNode("li", [LeafNode(None, "list line 2")]), ParentNode("li", [LeafNode(None, "list line 3")])])])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_ol(self):
        text = "1. list line 1\n2. list line 2\n3. list line 3"
        expected = ParentNode("div", [ParentNode("ol", [ParentNode("li", [LeafNode(None, "list line 1")]), ParentNode("li", [LeafNode(None, "list line 2")]), ParentNode("li", [LeafNode(None, "list line 3")])])])
        result = markdown_to_html_node(text)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node_mixedinline(self):
        text = "1. list **line** 1\n2. list line 2\n3. list *line* 3\n4. [link](https://www.google.com).\n5. ![alt text for image](url/of/image.jpg)"        
        expected = ParentNode("div", 
            [ParentNode("ol", 
                [ParentNode("li", 
                    [ParentNode(None, 
                        [LeafNode(None, "list ")]), 
                    ParentNode("b", 
                        [LeafNode(None, "line")]), 
                    ParentNode(None, 
                        [LeafNode(None, " 1")])]), 
                ParentNode("li", 
                    [ParentNode(None, 
                        [LeafNode(None, "list line 2")])]), 
                ParentNode("li", 
                    [ParentNode(None, 
                        [LeafNode(None, "list ")]), 
                    ParentNode("i", 
                        [LeafNode(None, "line")]), 
                    ParentNode(None, 
                        [LeafNode(None, " 3")])]), 
                ParentNode("li", 
                    [ParentNode("a", 
                        [LeafNode(None, "link")], {'href': 'https://www.google.com'}), 
                    ParentNode(None, 
                        [LeafNode(None, ".")])]), 
                ParentNode("li", 
                    [ParentNode("img", [], {'src': 'url/of/image.jpg', 'alt': 'alt text for image'})])])])
        result = markdown_to_html_node(text)
        apply_inline(result)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
