import pandas

# lists to hold ticket details
all_names = ["A", "B", "c", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}


# Create a table from dict
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Cacluate total payable for each tocket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()


print(mini_movie_frame)
print(f"Total Paind: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
