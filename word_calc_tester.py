# Landon Beach
# Date: 2/27/17
# A program that tests the adder function in the word_calc module.

# Import the adder function from the word_calc module.
from word_calc import adder

# Test cases that work.
print(adder('eight', 'nine'))
print(adder('Seven', 'ZERO'))
print(adder('Zero', 'zero'))
print(adder('ten', 'ten'))
print(adder('two', 'three'))
print(adder('nine', 'two'))
print(adder('three', 'four'))

# Test cases that don't work but are handled.
print(adder('eleven', 'ten'))
print(adder('one', 'steve'))
print(adder('eleven', 'steve'))
print(adder('thirteen', 'fourteen'))
print(adder('seven',0))
print(adder(11,'two'))
print(adder([1,2,3], [3,2,1]))

