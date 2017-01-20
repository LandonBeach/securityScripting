# Landon Beach
# Exercise 2.3

# Store a person's name in a variable, and print a message to that person.
name = "Eric Idle"
message = "Hello, " + name.title() + " would you like some spam?"
print(message)


# Landon Beach
# Exercise 2.4

# Store a person's name in a variable
# Print that person's name in lowercase, uppercase, and titlecase.
name = "Eric Idle"
print(name.lower())
print(name.upper())
print(name.title())


# Landon Beach
# Exercise 2.5

# Print a famous quote and the name of its author.
print('Ben Kenobi once said, "These are not the droids you are looking for".')


# Landon Beach
# Exercise 2.6

# Store a famous person's name in a variable called famous_person.
# Store a quote from that person in a variable called message.
# Print the message.
famous_person = "ben kenobi"
message = "These are not the droids you are looking for"
print(famous_person.title() + ' once said, "' + message + '"')


# Landon Beach
# Exercise 2.7

# Store a person's name with some whitespace characters at the beginning and end of the name.
# Print the name once with whitespace characters.
# Print the name using each of the three stripping functions. (lstrip, rstrip, strip)
name = "\t\t\n  Eric Idle  \t\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


# Landon Beach
# Exercise 2.9

# Store your favorite number in a variable.
# Create a message that reveals your favorite number.
# Print that message
favorite_number = 0
message = "My favorite number is " + str(favorite_number) + '.'
print(message)
