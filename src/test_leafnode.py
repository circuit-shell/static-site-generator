import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.to_html(), "<p>This is a leaf node</p>")

    def test_to_html_with_props(self):
        node = LeafNode("p", "This is a leaf node", {"class": "paragraph"})
        self.assertEqual(node.to_html(), '<p class="paragraph">This is a leaf node</p>')


if __name__ == "__main__":
    unittest.main()
