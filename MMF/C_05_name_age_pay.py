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
while True:
# Ask for name
    name = not_blank("Name: ")

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
