# Project Structure

## Classes Module
CompressionNode, or Node, is a class that represents a chunk of a compressed message. When creating an instance, the Node takes a name and the content/text, which is compressed into binary form. It also creates empty references to left and right children. Node also has a to_text() method that converts the content to readable text from binary.

CompressionTree, or Tree, is a class that holds multiple Node instances, and represents a message broken into chunks. When creating an instance, the Tree takes a name and the content/text for the root node. Tree also has two methods that use recursion:

- get() takes a name, and searches the Tree for a Node with that name. It then returns the binary content of that Node. If no Node exists with the provided name, it raises a ValueError.
- post_order() traverses the tree in the "left-right-current" order. For each Node it explores, it uses the to_text() method and stores the decompressed text in a list. This list is returned at the end.

## Main Module
The main function creates a Tree using text from user input. It then reads the content contained in the first two chunks created and completes a post-order-traversal.

This module also contains the following functions, used to make an organized Tree:

- compress_text() takes the message to be stored in the Tree, creates the Tree, and sends the root (which contains the full message) to the recursive method, build_tree().
- build_tree() is a recursive method. At the base case, when a provided Node is None, it does nothing. Otherwise, it takes the Node's content, and uses split_text() to gather new text chunks. These chunks are then placed into new nodes, which are assigned as the provided node's children. Lastly, build_tree() calls on itself again to repeat this process for the new chunks.
- split_text() takes a piece of text and splits it into two halves. It then returns a tuple with those halves. If the provided text has a length of 1, it returns a None tuple to imply the text cannot be halved any further.

## Tests Module
CompressionTests is a PyUnit-based class that tests multiple possible cases of a CompressionTree and its usage. It contains the following tests:

- test_odd_length() tests the creation of a tree with a message that has an even amount of characters. The used text is "Hello World", and it asserts that the first two subchunks created are "Hello " and "World". It also ensures that the post-order traversal includes "Hel", "Wor", and " ", but not "Bye World".
- test_even_length() tests the creation of a tree with a message that has an odd amount of characters. The used text is "ITSC2214", and it asserts that the first two subchunks created are "ITSC" and "2214". It also ensures that the post-order traversal includes "IT" and "22", but not " " and "ITSC2181".
- test_one_char() tests the creation of a tree with a message that has one character. The used text is "!", and it asserts that the root contains "!". It also ensures that the post-order traversal includes "!", but not "Hi".
- test_empty_string tests that the creation of a tree with an empty message is not possible. The used text is "", and it asserts that a ValueError is thrown with the appropriate message.
- test_nonexistent_chunk() tests an attempt to get the content at a chunk node that does not exist. It creates a tree with just the root containing "H". It tries to get a node whose name is "W" and asserts that a ValueError is thrown with the appropriate message.
