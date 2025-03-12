import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_node_not_eq(self):
		node = TextNode("This is a text", TextType.TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_node_url_is_none(self):
		node = TextNode("This is a text node", TextType.TEXT)
		self.assertEqual(node.url, None)

	def test_node_type_is_equal_to_bold(self):
		node = TextNode("This is a text bold node", TextType.BOLD)
		self.assertEqual(node.text_type, TextType.BOLD)

class TestTextNodeToHTMLNode(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
	
	def test_image(self):
		node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is an image"})
	
	def test_bold(self):
		node = TextNode("This is bold", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
	unittest.main()