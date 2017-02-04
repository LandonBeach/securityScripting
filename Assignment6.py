# Landon Beach
# 2/3/2017

try:
	# Ask for two integers from the user.
	num_1 = int(input("First number: "))
	num_2 =	int(input("Second number: "))

	# Check if first integer is less than the second integer.
	if num_1 < num_2:
		print("%d is less than %d." % (num_1, num_2))
	# Check if the first integer is greater than the second integer.
	elif num_1 > num_2:
		print("%d is greater than %d." % (num_1, num_2))
	# Else, the first integer is equal to the second number.
	else:
		print("%d is equal to %d." % (num_1, num_2))

# Handle if the user does not enter an integer
except ValueError:
	print("Please enter an integer")
