def round_ans(val):
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    answer = to_convert * 1.8 +32
    return round_ans(answer)
    


# Main routine
to_c_test = [0, 100, -459]
to_f_test = [0, 100, -40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()


for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} F is {ans} C")