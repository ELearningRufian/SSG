import functools
from parentnode import ParentNode
from leafnode import LeafNode
from inlineutils import text_to_textnodes
from nodeutils import text_node_to_html_node

def markdown_to_blocks(markdown):
    lines = (markdown.split("\n")) + [""]
    blocks = []
    blockbuilder = []
    for i in range(len(lines)):
        if "" == lines[i]:
            if 0 < len(blockbuilder):
                blocks.append(("\n".join(blockbuilder)).strip())
                blockbuilder = []
        else:
            blockbuilder.append(lines[i])
    return blocks

def block_to_block_type(block):
    if "###### " == block[:7]:
        return "h6"
    if "##### " == block[:6]:
        return "h5"
    if "#### " == block[:5]:
        return "h4"
    if "### " == block[:4]:
        return "h3"
    if "## " == block[:3]:
        return "h2"
    if "# " == block[:2]:
        return "h1"
    if ("```" == block[:3]) and ("```" == block[-3:]):
        return "code"
    lines = block.split("\n")
    if functools.reduce(lambda x,y: x and y, map(lambda x: ">" == x[0], lines)):
        return "blockquote"
    if functools.reduce(lambda x,y: x and y, map(lambda x: (x[0] in "*-") and x[1] == " ", lines)):
        return "ul"
    indices = list(map(lambda i: f"{i+1}. ", range(len(lines))))
    if functools.reduce(lambda x,y: x and y, map(lambda i: lines[i].startswith(indices[i]), range(len(lines)))):
        return "ol"
    return "p"
    
def strip_markdown(block, block_type):
    if "h" == block_type[0]:
        return block[1+int(block_type[1]):]
    if "code" == block_type:
        return block[3:-3] # TODO: html doesn't preserve newlines, multi-line code blocks do not result in a properly formatted paragraph
    if "blockquote" == block_type:
        return "\n".join(list(map(lambda l: (l[1:]).strip(" "), block.split("\n")))) # TODO: html doesn't preserve newlines, "\n".join does not result in a properly formatted paragraph
    if "l" == block_type[-1:]: # OL and UL should always be parents of LI items
        return None
    if "li" == block_type:
        return (block[1 + block.find(" "):]).strip(" ")
    return block
    
def apply_inline(root_node): # Do an **in-place replacement** of leaf nodes with the parent node that results from applying inline transformations
    for i in range(len(root_node.children)): 
        if isinstance(root_node.children[i], LeafNode): 
            root_node.children[i] = ParentNode((root_node.children[i]).tag, list(map(lambda n: text_node_to_html_node(n), text_to_textnodes((root_node.children[i]).value))), (root_node.children[i]).props)
        elif isinstance(root_node.children[i], ParentNode): # If a parent node, apply recursively to all children
            apply_inline(root_node.children[i])

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", children=[])
    for block in blocks:
        block_type = block_to_block_type(block)
        if "l" == block_type[-1:]: #unordered and ordered lists
            child = ParentNode(block_type, strip_markdown(block, block_type))
            lines = block.split("\n")
            grandchildren = []
            for line in lines:
                grandchildren.append(LeafNode("li", strip_markdown(line, "li")))
            child.children = grandchildren
        else:
            child = LeafNode(block_type, strip_markdown(block, block_type))
        parent.children.append(child)
    apply_inline(parent)
    return parent
        

        
    