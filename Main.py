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
        chars.append(entry[0].upper())
        freq.append(float(entry[1]))
file.close()
print("Chars:", chars)
print("Frequency:", freq)

tm.makeTree(nodes, chars, freq)

with open("binaryStrings.txt","r") as bin:
    for line in bin:
        binary_string = line
        decoded_text = tm.binarydecode(nodes[0], binary_string)
        print(f"Decoded Text: {decoded_text}")

with open("letterStrings.txt","r") as bin:
    for line in bin:
        input_string = line.upper()
        encoded_text = tm.encode(nodes[0], input_string)
        print(f"Encoded Text: {encoded_text}")
