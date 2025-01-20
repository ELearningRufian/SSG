from enum import Enum

class TextType(Enum):
    TEXT = "text"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)
    
    def __repr__(self):
        qt = ("", '"')[isinstance(self.text, str)]
        qu = ("", '"')[isinstance(self.url, str)]
        return f"TextNode({qt}{self.text}{qt}, {self.text_type}, {qu}{self.url}{qu})"
    
