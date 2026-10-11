class CompressionNode:
    def __init__(self, name, content):
        if len(content) == 0 or content is None:
            raise ValueError("Cannot compress an empty message.")
        self.name = name
        self.content = ' '.join(f"{ord(c):08b}" for c in content).replace("\x00", "").replace("\x01", "")
        self.left = None
        self.right = None
    #end init
    
    def to_text(self):
        bin_content = self.content.split(" ")
        return "".join(chr(int(b, 2)) for b in list(bin_content))
    #end to_text
#end CompressionNode

class CompressionTree:
    def __init__(self, root_name, root_text):
        self.root = CompressionNode(root_name, root_text)
    #end init

    def get_recursive(self, node, name):
        if node is None:
            return ""
        if node.name == name:
            return node.content
        return self.get_recursive(node.left, name) + self.get_recursive(node.right, name)
    def get(self, name):
        result = self.get_recursive(self.root, name)
        if result == "":
            raise ValueError("Node with name " + name + " not found.")
        return result
    #end get

    def post_order_recursive(self, node):
        if node is None:
            return []
        return (self.post_order_recursive(node.left) + 
            self.post_order_recursive(node.right) +
            [node.to_text()])
    def post_order(self):
        return self.post_order_recursive(self.root)
    #end post_order
#end CompressionTree