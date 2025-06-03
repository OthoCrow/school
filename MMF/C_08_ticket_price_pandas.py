import pandas

# Functions
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


def currency(x):
    # Formats as currency ($#.##)
    return "${:.2f}".format(x)

# Main routine

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

while True:
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
    pay_method = string_checker("Payment method: ", payment_list, num_letters=2)

    # Calculate surcharge
    # Cash
    if pay_method == "cash":
        surcharge = 0
    # Credit
    else:
        surcharge = ticket_price * surcharge



    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)



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


print(mini_movie_frame.to_string(index=False))
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")