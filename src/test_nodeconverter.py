import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from nodeconverter import text_node_to_html_node  # wherever your function lives


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        node = TextNode("Hello world", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello world")

    def test_text_type_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_text_type_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_text_type_code(self):
        node = TextNode("x = 5", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "x = 5")

    def test_text_type_link(self):
        node = TextNode("Example", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Example")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_text_type_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "cat.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "cat.png", "alt": "Alt text"}
        )

    def test_invalid_text_type_raises(self):
        class FakeType:
            value = "fake"

        node = TextNode("Bad", FakeType())
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()