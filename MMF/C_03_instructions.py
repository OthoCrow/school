# Functions
def make_statement(statement, decoration):
    """Emphasises headings by adding decorationg to the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

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

        print("Please choose yes or no")

def instructions():
    make_statement("Instructions", "ℹ️")
    print('''

    For each ticket holder enter ...
    - Their name
    - Their age
    - The payment method (cash / credit)

    The program will record the ticket sale and calculate the 
    ticket cost (and the profit).

    Once you have either sold all of the tickets or entered the 
    exit code ('xxx'), the program will display the ticket 
    sales information and write the data to a text file.

    It will also choose one lucky ticket holder who wins the 
    draw (their ticket is free).

    ''')

# Main routine

make_statement("Mini-Movie Fundraiser Program", "🍿")
print()

want_instructions = string_checker("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

print(f"\n program continues...")
