import unittest
from leafnode import LeafNode  # Change 'htmlnode' to your actual file name

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

    def test_no_tag_returns_value(self):
        node = LeafNode(tag=None, value="Hello world")
        self.assertEqual(node.to_html(), "Hello world")

    def test_with_tag_and_props(self):
        node = LeafNode(tag="p", value="Hello world", props={"class": "text"})
        self.assertEqual(node.to_html(), '<p class="text">Hello world</p>')

    def test_with_tag_no_props(self):
        node = LeafNode(tag="span", value="Hi there")
        self.assertEqual(node.to_html(), '<span>Hi there</span>')

if __name__ == "__main__":
    unittest.main()