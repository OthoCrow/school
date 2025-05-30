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



# Main routine

# Initialise variables
payment_list = ('cash', 'credit')

# Ticket Prices
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit surcharge %
CREDIT_SURCHARGE = 0.05

while True:
# Ask for name
    name = not_blank("Name: ")

    # Ask for age
    age = int_check("Age: ")

    # Check age
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child price = $7.50
    elif age <= 16:
        ticket_price = CHILD_PRICE
    
    # Adult Price = $10.50
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # Senior Price = $6.50
    elif 65 <= age <=120:
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


print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} \nso the surcharge is ${surcharge:.2f} \n The total payable is ${total_to_pay:.2f}")

