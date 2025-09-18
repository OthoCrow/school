def alpha_check(question):
    response = input("input: ").lower()
    check = response.isalpha()
    if check == True:
        return response
    else: 
        return "Please refrain from entering non-alphabetical characters."

# Main
while True:
    x = alpha_check("Input")
    print(x)