class HTMLNode():
    def __innit__(self, tag = None, value = None, children = None, props = None,):
        self.tag = tag #string
        self.value = value #string
        self.children = children #list of HTMLNode obj
        self.props = props #dictionary
    
    def to_html(self):
        raise NotImplementedError()

    