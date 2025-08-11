# Functions
def decode(text, shift=3):
    """Decrypt a users input using a single digit key between 1 and 26."""
    output = ""
    for c in text:
        if c == " ":
            output += " "
        if c in ALPHABET:
            index = ALPHABET.index(c)
            new_index = (index - shift) % len(ALPHABET)
            output += ALPHABET[new_index]
        else:
            output += "?"
    return output


# Variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
string = "cheud"

# Main routine
print(decode(string))