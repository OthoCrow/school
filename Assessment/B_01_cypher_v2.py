import itertools

# Functions go here
def make_statement(statement, decoration):
    """Emphasise headings by adding decoration to the start and end."""
    print(f"{decoration * 3} {statement} {decoration * 3}\n")


def string_checker(question, valid_answers=("yes", "no"), num_letters=1):
    """Check that user is a word from a list of valid responses."""
    while True:
        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the entire word
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
        print(
            "1. Choose whether you want to encode or decode a message.\n"
            "2. If encoding, enter the text you want to encrypt. If decoding, enter the text you want to decrypt.\n"
            "3. Enter a key (an integer between 1 and 25). This value determines how many positions each letter will be shifted in the alphabet.\n"
            "4. The program will display the encoded or decoded message based on your input.\n"
            "5. You can repeat the process or exit the program (enter xxx) after receiving your output and view history.")


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


# Constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
encoded_history = []
decoded_history =[]
to_encode_history = []
to_decode_history = []

# Main routine
instructions()

while True:
    encode_decode = string_checker("Do you want to encode or decode? ", valid_answers=("encode", "decode", "xxx"))

    # Exit loop
    if encode_decode == "xxx":
        break
    # Choose encode
    elif encode_decode == "encode":
        string = input("Enter text to encode: ").lower()
        to_encode_history.append(string)
        shift = int_check("Please enter an integer between 1 and 25 for shift: ", 1, 25)
        # Encodes string and prints output
        encoded_history.append(encode(string, shift))
        print(encoded_history[-1])
    # Choose decode
    elif encode_decode == "decode":
        string = input("Enter text to decode: ").lower()
        to_decode_history.append(string)
        shift = int_check("Please enter an integer between 1 and 25 for shift: ", 1, 25)
        # Decodes string and prints output
        decoded_history.append(decode(string, shift))
        print(decoded_history[-1])


# Formatting and printing of history
history_string = ""

for encode, encoded, decode, decoded in itertools.zip_longest(to_encode_history, encoded_history, to_decode_history, decoded_history):
    history_string += (
        f"Encode: {encode}  >>  {encoded}\n"
        f"Decode: {decode}  >>  {decoded}\n"
        "---------------------------\n"
    )

print(history_string)
