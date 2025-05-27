def not_blank(question):
    # Check if response is blank
    while True:
        response = input(question)
        if response != "":
            return
        else:
            print("Input is blank")


who = not_blank("Please enter your name: ")
print(f"{who}")