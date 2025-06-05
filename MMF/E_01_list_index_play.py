import random
fruit_list = ['apple', 'banana', 'cherry', 'dragon fruit']
colour_list = ['green', 'yellow', 'red', 'pink']

first_fruit = random.choice(fruit_list)

fruit_index = fruit_list.index(first_fruit)

first_color = colour_list[fruit_index]

print(f"fruit{first_fruit} -- color{first_color}")