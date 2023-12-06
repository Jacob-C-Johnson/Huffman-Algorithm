# Huffman tree build and methods provided by geeks for geeks examples
# Encode and Decode methods engineered using chat gpt
import heapq
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Function to encode a string using Huffman Tree nodes
def encode(root, input_str):
    encoded_str = ""
    char_to_code_mapping = {}

    # Generate a mapping of characters to their Huffman codes
    def generate_mapping(node, val=''):
        newVal = val + str(node.huff)
        if node.left:
            generate_mapping(node.left, newVal)
        if node.right:
            generate_mapping(node.right, newVal)
        if not node.left and not node.right:
            char_to_code_mapping[node.symbol] = newVal

    generate_mapping(root)
    # Encode the input string using the generated mapping
    for char in input_str:
        encoded_str += char_to_code_mapping[char]
    return encoded_str


# new decode function that goes from binary to a word
def binarydecode(root, binary_str):
    decoded_str = ""
    current_node = root

    for bit in binary_str:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        # If a leaf node is reached, append the symbol to the decoded string
        if not current_node.left and not current_node.right:
            decoded_str += current_node.symbol
            current_node = root  # Reset to the root for the next iteration
    return decoded_str


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    # if node is edge node then
    # display its huffman code
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


def makeTree(nodes, chars, freq):
    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        heapq.heappush(nodes, newNode)
    # Huffman Tree is ready!
    root_node = nodes[0]
    printNodes(root_node)
