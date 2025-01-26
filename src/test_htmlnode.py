import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HTMLNode(
            "a",
            "This is a anchor",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'


if __name__ == "__main__":
    unittest.main()
