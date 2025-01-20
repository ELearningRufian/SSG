import functools

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if None == self.props:
            return ""
        return functools.reduce(lambda x, y: x + y, map(lambda t: f' {t}="{self.props[t]}"', self.props))
    
    def __repr__(self):
        qt = ("", '"')[isinstance(self.tag, str)]
        qv = ("", '"')[isinstance(self.value, str)]
        return f"HTMLNode(tag={qt}{self.tag}{qt}, value={qv}{self.value}{qv}, children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        return (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props)

    
