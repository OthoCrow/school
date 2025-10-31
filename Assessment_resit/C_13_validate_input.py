def validate_input(prompt, length=None, max_length=None):
    # Checks that input is ascii characters (optionally specific lengths)
    while True:
        response = input(prompt).strip()
        if response.isascii() == False:
            print("Please enter characters only from the ascii character set: ")
            continue
        # Is equal to defined length
        if length != None and len(response) != length:
            print(f"Please enter {length} characters: ")
            continue
        # Is less than max length
        if max_length != None and len(response) > max_length:
            print(f"Please enter {max_length} characters or less: ")
            continue
        return response


# Main routine
# Loop for testing
while True:
    print(validate_input("Input: ", length=5))