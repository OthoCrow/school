# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # Exit code
    if name == "xxx":
        break
    else: 
        tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all of your tickets! {MAX_TICKETS}")
else:
    print(f"You have sold {tickets_sold} out of {MAX_TICKETS} tickets ({tickets_sold / MAX_TICKETS * 100}%).")