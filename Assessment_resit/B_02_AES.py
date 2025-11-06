# Constants
SBOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
    0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
    0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
    0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
    0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
    0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
    0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
    0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
    0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
    0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
    0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
    0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
    0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
    0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
    0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
    0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
    0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

INV_SBOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38,
    0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
    0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
    0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
    0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
    0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
    0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
    0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
    0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
    0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
    0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
    0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
    0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
    0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
    0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
    0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26,
    0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


# Functions go here
def make_statement(statement, decoration, amount=3):
    # Emphasise headings by adding decoration to the start and end.
    print(f"{decoration * amount} {statement} {decoration * amount}\n")


def string_checker(question, valid_answers=("yes", "no"), num_letters=1):
    # Check that user input is a word from a list of valid responses.
    while True:
        response = input(question).lower()

        for item in valid_answers:

            # Check if the response is the entire word
            if response == item:
                return item

            # Check if it is the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose from {valid_answers}\n")


def instructions():
    # Checks if user wants instructions
    want_instructions = string_checker("\nDo you want printed instructions?: ")

    if want_instructions == "yes":
        # Print instructions
        make_statement("Instructions", "#")
        print("""
            This program encrypts and decrypts using the Advanced Encryption
            Standard. Enter a 16 character key that will be used to encrypt
            your text, make sure that this is securely generated. You will
            be prompted for the plain text you want to encrypt, or ciphertext
            you want to decrpt(ensure that ciphertext is in same format as
            output from encryption). The program will print the output after
            it has run its operations.
            """)


def to_state():
    # Pads the user input and formats it into the 16 byte block
    if decrypt:
        # Converts input to a list
        try:
            ciphertext = validate_input("Enter ciphertext: ", None, 2600, 32)
            to_block = list(bytes.fromhex(ciphertext))
        except Exception as err:
            print("An error has occured: {err}")

    else:
        # Converts plaintext to list of bytes
        plaintext = validate_input("Enter plaintext: ", None, 1300, 1)
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


def g(word, round_num):
    # Used in key expansion
    # Shift byte
    word = word[1:] + word[:1]
    # Sub byte
    word = [SBOX[b] for b in word]
    # XOR RCON
    word[0] ^= RCON[round_num]
    return word


def expand_keys():
    # Expands original 128 bit key into 44 round keys
    key = list(validate_input("Enter 16 character key: ", 16).encode("utf-8"))
    # Splits key into "words"
    words = [key[i:i + 4] for i in range(0, 16, 4)]

    # Generates new keys
    for i in range(4, 44):
        temp = words[i - 1]
        if i % 4 == 0:
            temp = g(temp, (i // 4) - 1)
        new_word = [a ^ b for a, b in zip(temp, words[i-4])]
        words.append(new_word)

    # Formats keys in dictionary
    keys = {}
    for round_num in range(11):
        start = round_num * 4
        w0, w1, w2, w3 = words[start:start+4]

        keys[f"key{round_num}"] = w0 + w1 + w2 + w3
    return keys


def gmul(a, b):
    # GF(2^8) multiplication
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x11b
        a &= 0xFF
        b >>= 1
    return p


def sub_bytes(rows):
    # Substitutes bytes using the SBOX
    subbed = {}
    for r, row in rows.items():
        new_row = []
        for b in row:
            new_row.append(SBOX[b])
        subbed[r] = new_row
    return subbed


def shift_rows(subbed):
    # Shifts rows to the right
    shifted = {}
    shifted["row0"] = subbed["row0"]
    shifted["row1"] = subbed["row1"][1:] + subbed["row1"][:1]
    shifted["row2"] = subbed["row2"][2:] + subbed["row2"][:2]
    shifted["row3"] = subbed["row3"][3:] + subbed["row3"][:3]
    return shifted


def mix_columns(shifted, mixcolumns=True):
    # Mixes columns using method akin to matrice multiplication
    mixed = {"row0": [], "row1": [], "row2": [], "row3": []}
    for c in range(4):
        a0 = shifted["row0"][c]
        a1 = shifted["row1"][c]
        a2 = shifted["row2"][c]
        a3 = shifted["row3"][c]

        # Skips on last round
        if mixcolumns is True:
            col0 = gmul(a0, 2) ^ gmul(a1, 3) ^ gmul(a2, 1) ^ gmul(a3, 1)
            col1 = gmul(a0, 1) ^ gmul(a1, 2) ^ gmul(a2, 3) ^ gmul(a3, 1)
            col2 = gmul(a0, 1) ^ gmul(a1, 1) ^ gmul(a2, 2) ^ gmul(a3, 3)
            col3 = gmul(a0, 3) ^ gmul(a1, 1) ^ gmul(a2, 1) ^ gmul(a3, 2)
        else:
            col0 = a0
            col1 = a1
            col2 = a2
            col3 = a3

        mixed["row0"].append(col0)
        mixed["row1"].append(col1)
        mixed["row2"].append(col2)
        mixed["row3"].append(col3)

    return mixed


def inv_shift_rows(rows):
    # Reverse of shift rows
    shifted = {}
    shifted["row0"] = rows["row0"]
    shifted["row1"] = rows["row1"][-1:] + rows["row1"][:-1]
    shifted["row2"] = rows["row2"][-2:] + rows["row2"][:-2]
    shifted["row3"] = rows["row3"][-3:] + rows["row3"][:-3]
    return shifted


def inv_sub_bytes(shifted):
    # Substitutes bytes using the inverse SBOX
    subbed = {}
    for r, row in shifted.items():
        new_row = []
        for b in row:
            new_row.append(INV_SBOX[b])
        subbed[r] = new_row
    return subbed


def inv_mix_columns(subbed, mixcolumns=True):
    # Does the inverse of mix_columns by multiplying with the inverse set matrix
    mixed = {"row0": [], "row1": [], "row2": [], "row3": []}
    for c in range(4):
        a0 = subbed["row0"][c]
        a1 = subbed["row1"][c]
        a2 = subbed["row2"][c]
        a3 = subbed["row3"][c]

        # Skips on last round
        if mixcolumns is True:
            col0 = gmul(a0, 14) ^ gmul(a1, 11) ^ gmul(a2, 13) ^ gmul(a3, 9)
            col1 = gmul(a0, 9) ^ gmul(a1, 14) ^ gmul(a2, 11) ^ gmul(a3, 13)
            col2 = gmul(a0, 13) ^ gmul(a1, 9) ^ gmul(a2, 14) ^ gmul(a3, 11)
            col3 = gmul(a0, 11) ^ gmul(a1, 13) ^ gmul(a2, 9) ^ gmul(a3, 14)
        else:
            col0 = a0
            col1 = a1
            col2 = a2
            col3 = a3

        mixed["row0"].append(col0)
        mixed["row1"].append(col1)
        mixed["row2"].append(col2)
        mixed["row3"].append(col3)

    return mixed


def encryption(state, keys):
    # Perform operations to encrypt data
    # Add initial round key
    state = add_round_key(state, keys['key0'])
    for round_num in range(1, 11):
        temp_state = {}
        # Do mix_columns?
        if round_num == 10:
            mixcolumns = False
        else:
            mixcolumns = True

        for block_name, rows in state.items():

            # Sub bytes
            subbed = sub_bytes(rows)

            # Shift Rows
            shifted = shift_rows(subbed)

            # Mix Columns
            mixed = mix_columns(shifted, mixcolumns)

            # Add Round Key
            keyed = add_round_key({block_name: mixed}, keys[f'key{round_num}'])

            temp_state.update(keyed)
        # Use for next round
        state = temp_state
    # Use for output
    return state


def decryption(state, keys):
    # Perform operations to decrypt data
    # Add initial round key
    state = add_round_key(state, keys['key10'])

    for round_num in range(10, 0, -1):
        temp_state = {}
        # Do inv_mix_columns?
        if round_num == 1:
            mixcolumns = False
        else:
            mixcolumns = True

        for block_name, rows in state.items():
            # Inv Shift Rows
            shifted = inv_shift_rows(rows)

            # Inv Sub Bytes
            subbed = inv_sub_bytes(shifted)

            # Add Round Key
            keyed = add_round_key({block_name: subbed}, keys[f'key{round_num - 1}'])

            # Inv Mix Columns
            mixed = inv_mix_columns(keyed[block_name], mixcolumns)

            temp_state[block_name] = mixed
        # Use for next round
        state = temp_state
    # Use for output
    return state


def round_transformation(state, decrypt, keys):
    # Encryption
    if decrypt is False:
        new_state = encryption(state, keys)
    # Decryption
    else:
        new_state = decryption(state, keys)

    return new_state


def add_round_key(state, round_key):
    # Adds the round key
    new_state = {}
    for block_name, rows in state.items():
        new_rows = {}
        for r in range(4):
            new_row = []
            for c in range(4):
                key_index = r + 4 * c
                new_row.append(rows[f"row{r}"][c] ^ round_key[key_index])
            new_rows[f"row{r}"] = new_row
        new_state[block_name] = new_rows
    return new_state


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
make_statement("ENCRYPTION", "#", 5)
print(
    f"""    This is a program for encrypting and decrypting text. Encrypting is converting plain text into ciphertext (or a code), like spies do.
    That means that you can enter a word or multiple words and a key to encrypt it with.
    In the terms of encryption, a key is much like a physical key, you can lock and unlock your text with it.
    Enjoy!\n"""
)

instructions()
while True:
    decrypt = string_checker("\nWould you like to encrypt or decrypt?: ", valid_answers=("encrypt", "decrypt"))
    if decrypt == "decrypt":
        decrypt = True
    else:
        decrypt = False

    keys = expand_keys()
    state_array = to_state()

    state_array = round_transformation(state_array, decrypt, keys)

    output = []
    for block_name in state_array.values():
        for c in range(4):
            output.append(block_name["row0"][c])
            output.append(block_name["row1"][c])
            output.append(block_name["row2"][c])
            output.append(block_name["row3"][c])

    if decrypt:
        plaintext = bytes(output)
        print(plaintext.decode("utf-8").strip())
    else:
        ciphertext = bytes(output)
        print(ciphertext.hex())

    next_round = string_checker("\nGo again?: ")
    if next_round == "yes":
        continue
    else:
        break
