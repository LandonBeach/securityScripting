# Landon Beach
# Assignment 7
# 2/6/17

# Assignment 7-4
pizza_toppings = []
topping = ""

# Prompt the user to enter a series of pizza toppings until they enter 'quit' as a value.
# As they enter each topping, print a message saying you'll add that topping to their pizza.
while (topping.lower() != 'quit'):
	topping = input("Enter a topping ('quit' to exit): ")
	if topping.lower() != 'quit':
	pizza_toppings.append(topping.lower())
		print("I will add %s to your pizza." % topping)


# Assignment 7-8
# Create a list of sandwich orders called sandwich_orders.
sandwich_orders = ['tuna', 'blt', 'spam', 'bologna']

# Create an empty list called finished_sandwiches.
finished_sandwiches = []

# Loop through the list of sandwich orders
# Print a message for each order.
# As each sandwich is made, move it to the list of finished sanwiches.
for s in sandwich_orders:
	print("I made your %s sandwich " % s)
	finished_sandwiches.append(s)

# Print a message listing each sandwich that was made.
print("Sandwiches made: ")
for s in finished_sandwiches:
	print("\t" + s)
