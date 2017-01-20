# Landon Beach
# 1/13/17
# Assignment 3

# Create a list for my pizza toppings.
my_pizza_toppings = ['pepperoni','sausage','cheese','mushroom']

# Copy my pizza toppings to my friend's pizza toppings.
friend_pizza_toppings = list(my_pizza_toppings)

# Add 'peppers'to my pizza toppings.
my_pizza_toppings.append('peppers')

# Remove 'mushrooms' from my friend's pizza toppings.
friend_pizza_toppings.remove('mushroom')

# Add 'spam' to my friend's pizza toppings.
friend_pizza_toppings.append('spam')

# Print all of my pizza toppings to stdout.
print("My Pizza Toppings:")
for topping in my_pizza_toppings:
	print(topping)
	
# Print all of my friend's pizza toppings to stdout.
print("\nFriend Pizza Topping:")
for topping in friend_pizza_toppings:
	print(topping)
	
