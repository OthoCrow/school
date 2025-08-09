"""This program uses encrypts and decrypts a string using a key.

This prgram uses the caesar shift cipher to encrypt a string of
lowercase characters from the alphabet. It uses a single digit
key between 1 and 26cto encrypt an decrypt the text.
"""


# Functions go here
def make_statement(statement, decoration):
    """Emphasise headings by adding decoration to the start and end."""
    print(f"{decoration * 3} {statement} {decoration * 3}\n")


def string_checker(question, valid_answers=("yes", "no"), num_letters=1):
    """Check that user is a word from a list of valid responses."""
    while True:
        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the intire word
            if response == item:
                return item

            # Check if it is the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose from {valid_answers}")


def instructions():
    """Check if the user wants to see the instructions and print them."""
    want_instructions = string_checker("Do you want to see the instructions? ")

    if want_instructions == "yes":
        # Print instructions
        make_statement("Instructions", "#")
        print("Here are the instructions...")


def int_check(question, low, high):
    """Check that user enters an interger between two values."""
    error = f"Please enter an integer between {low} and {high}."
    while True:
        try:
            # Change input to a integer and check that is within range
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def encode(text, shift=3):
    """Encrypt a users input using a single digit key between 1 and 26."""
    output = ""
    for c in text:
        if c == " ":
            output += " "
        if c in ALPHABET:
            index = ALPHABET.index(c)
            new_index = (index + shift) % len(ALPHABET)
            output += ALPHABET[new_index]
        else:
            output += "?"
    return output


def decode(text, shift=0):
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


# Constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Main routine
instructions()

encode_decode = string_checker("Do you want to encode or decode? ", valid_answers=("encode", "decode"))

if encode_decode == "encode":
    string = input("Enter text to encode: ")
    shift = int_check("Please enter an integer between 1 and 25 for shift: ", 1, 25)
    # Encodes string and prints output
    print(encode(string, shift))

elif encode_decode == "decode":
    string = input("Enter text to decode: ")
    shift = int_check("Please enter an integer between 1 and 25 for shift: ", 1, 25)
    # Decodes string and prints output
    print(decode(string, shift))
