from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if None == self.value:
            raise ValueError("Leaf nodes MUST have a value")
        if None == self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
