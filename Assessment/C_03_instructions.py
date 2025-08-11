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
    # Print instructions
    make_statement("instructions", "ℹ️")
    print("Here are the instructions...")


# Main routine
want_instructions = string_checker("Do you want to see the instructions?")

if want_instructions == "yes": 
    instructions()