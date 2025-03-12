import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_valid_props_to_html(self):
		props = {
		    "href": "https://www.google.com",
		    "target": "_blank",
		}
		node = HTMLNode(props=props)
		self.assertEqual(node.props_to_html(), "href='https://www.google.com' target='_blank'")

	def test_values(self):
		node = HTMLNode("div", "I wish I could read")
		self.assertEqual(node.tag, "div")
		self.assertEqual(node.value, "I wish I could read")
		self.assertEqual(node.children, None)
		self.assertEqual(node.props, None)

	def test_equal_tag(self):
		node = HTMLNode(tag="p")
		self.assertEqual(node.tag, "p")

	def test_value_is_not_none(self):
		node = HTMLNode()
		self.assertEqual(node.value, None)

	def test_repr(self):
		node = HTMLNode("p", "What a strange world", None, { "class": "primary" })
		self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")

if __name__ == "__main__":
	unittest.main()