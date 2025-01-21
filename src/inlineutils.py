
import functools
import re
from textnode import TextType, TextNode

def split_node_delimiter(old_node, delimiter, text_type):
    if not old_node.text_type == TextType.TEXT:
        return [old_node]
    new_raw = old_node.text.split(delimiter)
    if 1 == len(new_raw):
        return [old_node] # No delimiters found
    if 0 == (len(new_raw)%2):
        raise SyntaxError(f"Invalid markdown. Missing closing delimiter in '{old_node.text}'")
    return list(map(lambda i: TextNode(new_raw[i], (TextType.TEXT, text_type)[i%2]), range(len(new_raw))))

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return list(functools.reduce(lambda l,m: l+m, list(map(lambda n: split_node_delimiter(n, delimiter, text_type), old_nodes))))

def extract_markdown_images(text):
    images_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"    
    return re.findall(images_regex, text)

def extract_markdown_links(text):
    links_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(links_regex, text)

def split_one(text, extractor, md_template, text_type):
    brk = extractor(text)
    if 0 == len(brk):
        return ([TextNode(text, TextType.TEXT)], "")
    markdown = f"{md_template[0]}{brk[0][0]}{md_template[1]}{brk[0][1]}{md_template[2]}"
    i = text.find(markdown)
    if 0 == i:
        return ([TextNode(brk[0][0], text_type, brk[0][1])], text[len(markdown):])
    return ([TextNode(text[0:i], TextType.TEXT),TextNode(brk[0][0], text_type, brk[0][1])], text[i+len(markdown):])

def split_node(old_node, extractor, md_template, text_type):
    if not old_node.text_type == TextType.TEXT:
        return [old_node]
    remainder = old_node.text
    nodes = []
    while 0 < len(remainder):
        new_nodes,remainder = split_one(remainder, extractor, md_template, text_type)
        nodes.extend(new_nodes)
    return nodes

def split_nodes_image(old_nodes):
    return list(functools.reduce(lambda l,m: l+m, list(map(lambda n: split_node(n, extract_markdown_images,("![","](",")"), TextType.IMAGE), old_nodes))))

def split_nodes_link(old_nodes):
    return list(functools.reduce(lambda l,m: l+m, list(map(lambda n: split_node(n, extract_markdown_links,("[","](",")"), TextType.LINK), old_nodes)),[]))

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    after_bold = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    after_italic = split_nodes_delimiter(after_bold, "*", TextType.ITALIC)
    after_code = split_nodes_delimiter(after_italic, "`", TextType.CODE)
    after_image = split_nodes_image(after_code)
    return split_nodes_link(after_image)