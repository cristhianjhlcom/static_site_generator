from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for idx in range(len(sections)):
            if sections[idx] == "":
                continue
            if idx % 2 == 0:
                split_nodes.append(TextNode(sections[idx], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[idx], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
