# Landon Beach
# 1/30
# Simple addition calculator

try:
	num1 = int(input("First Number: "))
	num2 = int(input("Second Number: "))
	print(num1 + num2)

except ValueError:
	print("Please enter in the form of an integer 0 - 9")

