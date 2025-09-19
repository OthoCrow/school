def alpha_check(question):
        # Checks that input is alphabetical characters
    response = input(question).lower()
    check = response.isalpha()
    if check == True:
        return response
    else: 
        return "Please refrain from entering non-alphabetical characters."


def to_state():
    # Converts plaintext to hexidecimal bytes
    plaintext = alpha_check("Enter plaintext: ")
    utf8_bytes = plaintext.encode("utf-8")
    hex_bytes = [format(b, '02x') for b in utf8_bytes]
    # Adds padding so each block is 16 bytes
    length = len(hex_bytes)
    padding_amount = 16 - length % 16
    padding = bytes([padding_amount]) * padding_amount
    return hex_bytes + [format(b, '02x') for b in padding]


# Main routine
print(to_state())