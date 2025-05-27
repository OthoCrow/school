# Functions
def string_checker(question, valid_ans_list, num_letters):
    # Checks that user enters full word or the first letter of a word from a selcetin of valid responses
    while True:
        response = input(question).lower()

        for item in valid_ans_list:

            # Check if the response is the intire word
            if response == item:
                return item

            # Check if it is the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# main routine 
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_checker("Do you like coffee?", yes_no_list, num_letters=1) 

print(f"You chose {like_coffee}")

pay_method = string_checker("Payment method: ", payment_list, num_letters=2)
print(f"You chose {pay_method}")