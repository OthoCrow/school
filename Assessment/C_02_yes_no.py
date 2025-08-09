# Functions
def string_checker(question):
    # Checks that user enters full word or the first letter of a word from a selcetin of valid responses
    while True:
        response = input(question).lower()

        for item in ["yes", "no"]:
            if response == item:
                return item
            elif response == item[0]:
                return item
        print(f"Please choose an option from y/n")

# main routine
while True:
    cool = string_checker("Are you cool?")
    print(cool)
