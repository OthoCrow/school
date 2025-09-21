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
    deci_bytes = list(utf8_bytes)
    # Adds padding so each block is 16 bytes
    length = len(deci_bytes)
    padding_amount = 16 - length % 16
    padding = bytes([padding_amount]) * padding_amount
    padded_bytes = deci_bytes + list(padding)
    block_dicts = {}
    for block_index in range(0, len(padded_bytes), 16):
        block_num = block_index // 16
        block = padded_bytes[block_index:block_index+16]
        rows = {
            "row0": block[0:4],
            "row1": block[4:8],
            "row2": block[8:12],
            "row3": block[12:16],
        }
        block_dicts[f"block{block_num}"] = rows
    return block_dicts


# Main routine
print(to_state())