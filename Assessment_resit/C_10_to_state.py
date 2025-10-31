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


def to_state(decrypt):
    # Pads the user input and formats it into the 16 byte block
    if decrypt:
        # Converts input to a list
        ciphertext = input("Enter ciphertext: ")
        to_block = list(bytes.fromhex(ciphertext))
    else:
        # Converts plaintext to list of bytes
        plaintext = validate_input("Enter plaintext: ")
        utf8_bytes = plaintext.encode("utf-8")
        list_bytes = list(utf8_bytes)
        # Adds padding so each block is 16 bytes
        length = len(list_bytes)
        padding_amount = 16 - length % 16
        padding = [padding_amount] * padding_amount
        to_block = list_bytes + padding

    # Arranges input into state
    blocks_dict = {}
    for block_index in range(0, len(to_block), 16):
        block_num = block_index // 16
        block = to_block[block_index:block_index+16]
        rows = {
            "row0": [block[0], block[4], block[8], block[12]],
            "row1": [block[1], block[5], block[9], block[13]],
            "row2": [block[2], block[6], block[10], block[14]],
            "row3": [block[3], block[7], block[11], block[15]],
        }

        blocks_dict[f"block{block_num}"] = rows
    return blocks_dict


# Main routine
while True:
    decrypt = validate_input("Encrypt or decrypt: ")
    if decrypt == "decrypt":
        decrypt = True
    else:
        decrypt = False

    print(to_state(decrypt))