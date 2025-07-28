# Functions
def decode(text, shift=3):
    output = ""
    for c in text:
        if c in alphabet:
            index = alphabet.index(c)
            new_index = (index - shift) % len(alphabet)
            output += alphabet[new_index]
        else:
            output += "?"
    return output

# Variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3
string = "cheud"

# Main routine
print(decode(string))