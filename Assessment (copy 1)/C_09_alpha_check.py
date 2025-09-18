def only_alpha(question):
    response = input(question).lower()
    check = response.isalpha()
    if check == False:
        print("Please refrain from using non-alphabetical characters")
    else:
        return response

# Main routine
x = only_alpha("question")
print(x)