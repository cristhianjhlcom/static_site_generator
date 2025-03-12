import unittest

from textnode import TextNode, TextType

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


if __name__ == "__main__":
	unittest.main()