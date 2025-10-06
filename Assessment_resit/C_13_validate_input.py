def validate_input(prompt, length=None):
    # Checks that input is alphabetical characters
    response = input(prompt).strip().lower()
    while True:
        if response.isascii() == False:
            return "Please enter characters only from the ascii character set: "
        if length != None and len(response) > length:
            return f"Please enter {length} characters or less: "
        return response


# Main routine
# Loop for testing
while True:
    print(validate_input("Input: ", length=5))