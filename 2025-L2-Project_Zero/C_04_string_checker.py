# Functions
def string_checker(question, valid_ans_list):
    # Checks that user enters full word oor the first letter of a word from a selcetin of valid responses
    while True:
        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item
            elif response == item[0]:
                return item
        print(f"Please choose an option from {valid_ans_list}")

# main routine 
levels = ["easy", "medium", "hard"]

# like_coffee = string_checker("Do you like coffee?", ["yes", "no"]) 

choose_level = string_checker("Choose a level: ", levels)
print(f"You chose {choose_level}")