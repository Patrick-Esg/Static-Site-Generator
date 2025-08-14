from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("no value created")
        if self.children is None:
            raise ValueError("no children created")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        # Wrap with opening and closing tag
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"