# Functions go here

def make_statement(statement, decoration):
    # Emphasises headings by adding decorationg to the start and end

    print(f"{decoration * 3} {statement} {decoration * 3}\n")

def string_checker(question, valid_answers=("yes", "no"), num_letters=1):
    # Checks that user enters full word or the first letter of a word from a selcetin of valid responses
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
    want_instructions = string_checker("Do you want to see the instructions? ")

    if want_instructions == "yes":
        # Print instructions
        make_statement("Instructions", "ℹ️")
        print("Here are the instructions...")

    # Checks that user enters an interger between two values

def int_check(question, low, high): 
    error = f"Please enter an integer between {low} and {high}."

    while True:
        try:
            # Change input to a inteer and check that is within range
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def encode(text, shift=3):
    shift = int_check(input("Please enter an integer between 1 and 25 for shift: "), 1, 25)
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
    shift = int_check(input("Please enter an integer between 1 and 25 for shift: "), 1, 25)
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
    # Encodes string and prints output
    print(encode(string))
    
elif encode_decode == "decode":
    string = input("Enter text to decode: ")
    # Decodes string and prints output
    print(decode(string))