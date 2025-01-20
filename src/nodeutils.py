from textnode import TextType
from leafnode import LeafNode

# These are utility functions written as as standalone functions (instead of as methods in TextNode) to better suit functional techniques
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src": text_node.url,"alt": text_node.text})
    raise ValueError("invalid text_node.text_type")

