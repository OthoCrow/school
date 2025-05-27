# Functions
def int_check(question, exit_code=None): 
    # Checks users enter an integer 

    error = "Please enter an integer"

    while True:
        try:
            # Return the response if its an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine

# loop for testing
while True:
    print()

    name = input("Name: ")

    age = int_check("Age: ")

    # Check age of user
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
