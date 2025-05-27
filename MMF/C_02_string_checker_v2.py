# Functions
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

        print(f"Please choose an option from {valid_answers}")

# main routine 
payment_list = ('cash', 'credit')

want_instructions = string_checker("Do you want to see the instructions? ")
print(f"You chose {want_instructions}")

pay_method = string_checker("Payment method: ", payment_list, num_letters=2)
print(f"You chose {pay_method}")