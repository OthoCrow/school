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

def int_check(question): 
    # Checks users enter an integer 

    error = "Please enter an integer"

    while True:
        try:
            # Return the response if its an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)

def not_blank(question):
    # Check if response is blank
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("Input is blank")

# Main routine

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0


make_statement("Mini-Movie Fundraiser Program", "🍿")
print()

want_instructions = string_checker("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()


while tickets_sold < MAX_TICKETS:
    # Ask for name
    name = not_blank("\nName: ")

    # Exit code
    if name == "xxx":
        break
    else:
            # Ask for age
        age = int_check("Age: ")

        # Check age
        if age < 12:
            print(f"{name} is too young")
            continue
        elif age > 120:
            print(f"{name} is too old")
            continue
        else:
            pass

        # Ask for payment method
        payment_list = ('cash', 'credit')

        pay_method = string_checker("Payment method: ", payment_list, num_letters=2)
        print(f"You chose {pay_method}")

        print(f"{name} has bought a ticket ({pay_method})")

        tickets_sold += 1



if tickets_sold == MAX_TICKETS:
    print(f"\nYou have sold all of your tickets! {MAX_TICKETS}")
else:
    print(f"\nYou have sold {tickets_sold} out of {MAX_TICKETS} tickets ({tickets_sold / MAX_TICKETS * 100}%).")
