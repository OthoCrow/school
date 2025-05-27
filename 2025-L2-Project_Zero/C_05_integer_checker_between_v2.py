# Functions
def int_check(question, low, high): 
    # Checks that user enters an interger between two values

    error = f"Please enter an integer between {low} and {high}."

    while True:

        try:
            # Change input to a inteer and check that is within range
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine

# loop for testing
while True:
    print()

    # ask user for an integer
    my_num = int_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")