# Landon Beach
# Assignment 4
# 1/20/17

# 1. Complete Exercise 6-1
# Create a dictionary of yourself.
my_info = {
        "first": "landon",
        "last": "beach",
        "city": "cedar city"
}

# Print the entire dictionary.
print(my_info)

# Print the keys and values separately in a readable format.
for n,v in my_info.items():
    print(n.title() + ": " + v.title())


# 2. Complete Exercise 6-3
print("")

# Create a glossary of five terms you have learned.
glossary = {
        "tuple": "a comma-separated sequence of values in Python that cannot be changed after it has been created.",
        "key-value pair": "a pair with a key and an associated value. The are often used in dictionaries in Python.",
        "word3": "DEFINITION3", # TODO: Come up with more words and definitions. 
        "word4": "DEFINITION4",
        "word5": "DEFINITION5"
        }

# Print the entire dictionary
print(glossary)

# Print the word and definition separately in a readable format.
for n,v in glossary.items():
    print("Word: " + n)
    print("Definition: " + v)


# 3. Complete Exercise 6-7
print("")

# Make two new dictionaries representing different people.
person1 = {
        "first": "eric",
        "last": "foreman",
        "city": "point place"
}
person2 = {
        "first": "scott",
        "last": "pilgrim",
        "city": "toronto"
}

# Store all three dictionaries in a list called people.
people = []
people.append(my_info)
people.append(person1)
people.append(person2)

# Print everything you know about each person in a readable format.
for p in people:
        for n,v in p[i].items():
                print(n + ": " + v)
        print("")

# TODO: The last problem for this assignment.
