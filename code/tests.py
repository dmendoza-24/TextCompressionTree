import unittest
from classes import CompressionNode as Node
from classes import CompressionTree as Tree
from main import compress_text

class CompressionTests(unittest.TestCase):
    def test_odd_length(self):
        compression = compress_text("Hello World")
        self.assertEqual(compression.root.name, "message.txt")

        # Subchunk-1 should contain 'Hello '
        self.assertEqual(compression.get("Subchunk-1"),
            "01001000 01100101 01101100 01101100 01101111 00100000")
        self.assertEqual(compression.get("Subchunk-1"),
            Node('test', 'Hello ').content)

        #Subchunk-2 should contain 'World'
        self.assertEqual(compression.get("Subchunk-2"),
            "01010111 01101111 01110010 01101100 01100100")
        self.assertEqual(compression.get("Subchunk-2"),
            Node('test', 'World').content)
        
        inorder = compression.post_order()
        self.assertIn("Hel", inorder)
        self.assertIn("Wor", inorder)
        self.assertIn(" ", inorder)
        self.assertFalse("Bye World" in inorder)
        self.assertEqual(len(inorder), 21)
    #end test_even

    def test_even_length(self):
        compression = compress_text("ITSC2214")
        self.assertEqual(compression.root.name, "message.txt")

        # Subchunk-1 should contain 'ITSC'
        self.assertEqual(compression.get("Subchunk-1"),
            "01001001 01010100 01010011 01000011")
        self.assertEqual(compression.get("Subchunk-1"),
            Node('test', 'ITSC').content)

        #Subchunk-2 should contain '2214'
        self.assertEqual(compression.get("Subchunk-2"),
            "00110010 00110010 00110001 00110100")
        self.assertEqual(compression.get("Subchunk-2"),
            Node('test', '2214').content)
        
        inorder = compression.post_order()
        self.assertIn("IT", inorder)
        self.assertIn("22", inorder)
        self.assertFalse(" " in inorder)
        self.assertFalse("ITSC2181" in inorder)
        self.assertEqual(len(inorder), 15)
    #end test_odd

    def test_one_char(self):
        compression = compress_text("!")
        self.assertEqual(compression.root.name, "message.txt")

        self.assertEqual(compression.root.content, "00100001")
        self.assertEqual(compression.get('message.txt'), "00100001")
        
        inorder = compression.post_order()
        self.assertIn("!", inorder)
        self.assertFalse("Hi" in inorder)
        self.assertEqual(len(inorder), 1)
    #end test_one

    def test_empty_string(self):
        try:
            compression = compress_text("")
        except ValueError as e:
            self.assertEqual(str(e), "Cannot compress an empty message.")
    #end test_empty

    def test_nonexistent_chunk(self):
        compression = compress_text("H")
        try:
            compression.get("W")
        except ValueError as e:
            self.assertEqual(str(e), "Node with name W not found.")
    #end test_non
#end Tests

if __name__ == "__main__":
    unittest.main()
#end main_test