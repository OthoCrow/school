import pandas
import random


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

def currency(x):
    # Formats as currency ($#.##)
    return "${:.2f}".format(x)

# Main routine

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0


make_statement("Mini-Movie Fundraiser Program", "🍿")
print()

want_instructions = string_checker("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()


# Initialise variables
payment_list = ('cash', 'credit')

# Ticket Prices
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit surcharge %
surcharge = 0.05


# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []


# Dict for ticket details
mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

while tickets_sold < MAX_TICKETS:
    # Ask for name
    name = not_blank("\nName: ")

    # Exit code
    if name == "xxx":
        break

    # Ask for age
    age = int_check("Age: ")


    # Check age
    if age < 12:
        print(f"{name} is too young")
        continue
    # Child price = $7.50
    elif age < 16:
        ticket_price = CHILD_PRICE
    # Adult Price = $10.50
    elif age < 65:
        ticket_price = ADULT_PRICE
    # Senior Price = $6.50
    elif age <=120:
        ticket_price = SENIOR_PRICE
    # Too old
    else:
        print(f"{name} is too old")
        continue


    # Ask for payment method
    payment_list = ('cash', 'credit')

    pay_method = string_checker("Payment method: ", payment_list, num_letters=2)
    print(f"You chose {pay_method}")

    print(f"{name} has bought a ticket ({pay_method})")

    # Calculate surcharge
    # Cash
    if pay_method == "cash":
        surcharge = 0
    # Credit
    else:
        surcharge = ticket_price * surcharge


    # Add names, cost and surcharge to list
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# Create a table from dict
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Cacluate total payable for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Calculate revenue and profit
print(mini_movie_frame.to_string(index=False))
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

# Choose random winner
winner = random.choice(all_names)

# Find index of winner
winner_index = all_names.index(winner)
print(f"Winner: {winner}, List Position: {winner_index}")

# Retrieve total won
total_won = mini_movie_frame.at[winner_index, 'Total']

# Winner announcment
print(f"The winner is {winner}. Their ticket worth ${total_won:.2f} is free!")

if tickets_sold == MAX_TICKETS:
    print(f"\nYou have sold all of your tickets! {MAX_TICKETS}")
else:
    print(f"\nYou have sold {tickets_sold} out of {MAX_TICKETS} tickets ({tickets_sold / MAX_TICKETS * 100}%).")
