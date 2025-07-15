# Functions go here
def make_statement(statement, decoration):
    # Emphasises headings by adding decorationg to the start and end

    print(f"{decoration * 3} {statement} {decoration * 3}\n")


def yes_no_checker(question):
    # Checks that user enters full word or the first letter of a word from a selcetin of valid responses
    while True:
        response = input(question).lower()

        for item in ["yes", "no"]:
            if response == item:
                return item
            elif response == item[0]:
                return item
        print(f"Please choose an option from y/n")

def instructions():
    # Print instructions
    make_statement("instructions", "ℹ️")
    print("Here are the instructions...")


# Main routine
want_instructions = string_checker("Do you want to see the instructions?")

if want_instructions == "yes": 
    instructions()