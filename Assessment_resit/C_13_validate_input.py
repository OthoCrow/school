def validate_input(prompt, length=None, max_length=None, min_length=None):
    # Checks that input is ascii characters (optionally specific lengths, max_length, min length)
    while True:
        response = input(prompt).strip()
        if response.isascii() is False:
            print("Input must only contain ascii characters\n")
            continue
        # Is equal to defined length
        elif length is not None and len(response) != length:
            print(f"Input must be {length} characters long\n")
            continue
        # Is less than max length
        elif max_length is not None and len(response) > max_length:
            print(f"Input must be {max_length} characters or less\n")
            continue
        elif min_length is not None and len(response) < min_length:
            print(f"Input must {min_length} characters or more\n")
            continue
        return response


# Main routine
# Loop for testing
while True:
    print(validate_input("Input: ", length=5))