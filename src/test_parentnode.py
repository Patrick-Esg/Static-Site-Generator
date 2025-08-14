import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "Hello")
        child2 = LeafNode("p", "World")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><p>Hello</p><p>World</p></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_nested_parentnodes(self):
        deep_child = LeafNode(None, "deep text")
        mid_node = ParentNode("section", [deep_child])
        top_node = ParentNode("div", [mid_node])
        self.assertEqual(top_node.to_html(), "<div><section>deep text</section></div>")

    def test_no_tag_raises(self):
        child_node = LeafNode("p", "child")
        with self.assertRaises(ValueError) as cm:
            ParentNode(None, [child_node])
        self.assertEqual(str(cm.exception), "ParentNode must have a tag.")

    def test_no_children_raises(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode("div", None)
        self.assertEqual(str(cm.exception), "ParentNode must have children.")

    def test_empty_children_list_raises(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode("div", [])
        self.assertEqual(str(cm.exception), "ParentNode must have children.")

if __name__ == "__main__":
    unittest.main()
