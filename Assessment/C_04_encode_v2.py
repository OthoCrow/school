# Functions
def encode(text, shift=3):
    """Encrypt a users input using a single digit key between 1 and 26."""
    output = ""
    for c in text:
        if c == " ":
            output += " "
        elif c in ALPHABET:
            index = ALPHABET.index(c)
            new_index = (index + shift) % len(ALPHABET)
            output += ALPHABET[new_index]
        else:
            output += "?"
    return output

# Variables
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
string = input("Input text to encode: ")

# Main routine
while True:
    print(encode(string))
    