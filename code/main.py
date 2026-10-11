from classes import CompressionNode as Node
from classes import CompressionTree as Tree

def compress_text(text:str):
    tree = Tree("Subchunk", text)
    build_tree(tree.root)
    tree.root.name = "message.txt"
    return tree
#end compress_text

def build_tree(node):
    # print(node.to_text())
    if node is None:
        return
    first_half, second_half = split_text(node.to_text())
    left = right = None
    if first_half is not None:
        left = Node(node.name+"-1", first_half)
    if second_half is not None:
        right = Node(node.name+"-2", second_half)
    node.left = left
    node.right = right
    build_tree(node.left)
    build_tree(node.right)
#end build_tree

def split_text(text:str):
    if len(text) == 1:
        return None, None
    midpoint = (len(text) + 1 ) // 2
    first_half = text[:midpoint]
    second_half = text[midpoint:]
    return (first_half, second_half)
#end split_text

def main(text):
    compression = compress_text(text)
    print("Root reads:", compression.get("message.txt"))
    if compression.root.left is not None:
        print("Subchunk-1 reads:", compression.get("Subchunk-1"))
        print("Subchunk-2 reads:", compression.get("Subchunk-2"))
    # print("Subchunk-1-1 reads:", compression.get("Subchunk-1-1"))
    # print("Subchunk-2-2 reads:", compression.get("Subchunk-2-2"))
    # print("Subchunk-2-2-1-2 reads:", compression.get("Subchunk-2-2-1-2"))
    print("\nTraversing the compression:")
    print(" -> ".join(compression.post_order()))
if __name__ == "__main__":
    text = input("Provide a small piece of text to compress: ")
    main(text)
    # print(split_text(text))
#end main