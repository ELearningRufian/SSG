from functools import reduce
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if None == self.tag:
            raise ValueError(f"Missing tag: {str(self)}")
        if None == self.children:
            raise ValueError(f"Missing children: {str(self)}")
        children_html = reduce(lambda s, t: s + t, map(lambda c: c.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
