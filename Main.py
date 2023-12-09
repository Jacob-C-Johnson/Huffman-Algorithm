import TreeMethods as tm

# list containing unused nodes
nodes = []
# characters for huffman tree
chars = []
# frequency of characters
freq = []

# Open the data file
with open("dataTeamX.txt", "r") as file:
    for line in file:
        entry = line.split()
        chars.append(entry[0].upper())
        freq.append(float(entry[1]))
file.close()
# Print the characters and frequency
print("Chars:", chars)
print("Frequency:", freq)

# Call the func that will make the huffman tree
tm.makeTree(nodes, chars, freq)

# open the binary stings file to decode them for each line in the file
with open("binaryStrings.txt","r") as bin:
    for line in bin:
        binary_string = line
        decoded_text = tm.binarydecode(nodes[0], binary_string)
        print(f"Decoded Text: {decoded_text}")

# open the letter strings to encode them for each line in the file
with open("letterStrings.txt","r") as bin:
    for line in bin:
        input_string = line.upper()
        encoded_text = tm.encode(nodes[0], input_string)
        print(f"Encoded Text: {encoded_text}")
