from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if None == self.value:
            raise ValueError("Leaf node MUST have a value")
        if None == self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        qt = ("", '"')[isinstance(self.tag, str)]
        qv = ("", '"')[isinstance(self.value, str)]
        props_str = ""
        if not None == self.props:
            props_str = f", {self.props}"
        return f"LeafNode({qt}{self.tag}{qt}, {qv}{self.value}{qv}{props_str})"