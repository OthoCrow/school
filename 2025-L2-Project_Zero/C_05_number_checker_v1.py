# Functions
def num_check(question, num_type, exit_code=None): 
    # Checks users enter an integer that is more than zero (or the 'xxx' exit code)

    if num_type == "integer":
        error = " Please enter an integer more than zero"
        change_to = int
    else:
        error = "Please enter a number more than zero"
        change_to = float

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine

# loop for testing
while True:
    print()

    my_float = num_check("Please enter a number more than 0: ", "float")
    print(f"You chose: {my_float}")
    print()
    my_int = num_check("Please enter an integer more than 0: ", "integer", "")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"You chose {my_int}")