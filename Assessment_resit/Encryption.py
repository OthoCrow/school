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

RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


# Functions
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
    padding = [padding_amount] * padding_amount
    padded_bytes = deci_bytes + padding
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


def g(word, round_num):
    # Shift byte
    word = word[1:] + word[:1]
    # Sub byte
    word = [SBOX[b] for b in word]
    # XOR RCON
    word[0] ^= RCON[round_num]
    return word

# Expands original 128 bit key into 44 round keys
def expand_keys():
    key = list("hhhheeeeuuuudddd".encode("utf-8"))
    # key = list(input("Enter key: ").encode("utf-8"))
    # Splits key into "words"
    words = [key[i:i +4] for i in range(0, 16, 4)]
    
    # Generates new keys
    for i in range (4, 44):
        temp = words[i -1]
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

# GF(2^8) multiplication
def gmul(a, b):
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


def round_transformation(state, mixcolumns):
    new_state = {}
    for block_name, rows in state.items():

        # SubBytes
        subbed = {}
        for r, row in rows.items():
            new_row = []
            for b in row:
                new_row.append(SBOX[b])
            subbed[r] = new_row

        # ShiftRows
        shifted = {}
        shifted["row0"] = subbed["row0"]
        shifted["row1"] = subbed["row1"][1:] + subbed["row1"][:1]
        shifted["row2"] = subbed["row2"][2:] + subbed["row2"][:2]
        shifted["row3"] = subbed["row3"][3:] + subbed["row3"][:3]

        # MixColumns
        mixed = {"row0": [], "row1": [], "row2": [], "row3": []}
        for c in range(4):
            a0 = shifted["row0"][c]
            a1 = shifted["row1"][c]
            a2 = shifted["row2"][c]
            a3 = shifted["row3"][c]

            if mixcolumns == True:
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

        new_state[block_name] = mixed

    return new_state


def add_round_key(state, round_key):
    new_state = {}
    for block_name, rows in state.items():
        new_rows = {}
        for r in range(4):
            new_row = []
            for c in range(4):
                key_index = r * 4 + c
                new_row.append(rows[f"row{r}"][c] ^ round_key[key_index])
            new_rows[f"row{r}"] = new_row
        new_state[block_name] = new_rows
    return new_state


# Main routine
state_array = to_state()
keys = expand_keys()
state_array = add_round_key(state_array, keys['key0'])

for round_num in range(1, 11):
    if round_num < 10:
        mixcolumns = True
    else: 
        mixcolumns = False

    state_array = round_transformation(state_array, mixcolumns)
    state_array = add_round_key(state_array, keys[f'key{round_num}'])

output = []
for block_name in state_array:
    block = state_array[block_name]
    for row_index in range(4):
        row_name = f"row{row_index}"
        for value in block[row_name]:
            output.append(value)

ciphertext = bytes(output)
print(ciphertext.hex())
