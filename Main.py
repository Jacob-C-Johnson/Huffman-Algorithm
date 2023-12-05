# A Huffman Tree Node
import heapq
import TreeMethods as tm

# list containing unused nodes
nodes = []
# characters for huffman tree
chars = []
# frequency of characters
freq = []
with open("dataTeamX.txt", "r") as file:
    for line in file:
        entry = line.split()
        chars.append(entry[0])
        freq.append(float(entry[1]))
file.close()
print("Chars:", chars)
print("Frequency:", freq)

tm.makeTree(nodes, chars, freq)

# Example: Decoding a binary string
binary_string = "110001001101"
decoded_text = tm.binarydecode(nodes[0], binary_string)
print(f"\nDecoded Text: {decoded_text}")

# Example: Encoding to a binary string
input_string = "FACE"
encoded_text = tm.encode(nodes[0], input_string)
print(f"\nEncoded Text: {encoded_text}")

if binary_string == encoded_text:
    print("Success")
