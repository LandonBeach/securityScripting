# Landon Beach
# Date: 2/27/17
# An adder function that takes two integers as words between zero and ten
# and returns the sum of the two integers as a word.

def adder(first_num='one', second_num='two'):
	''' Takes two string arguments whose values are a word between zero and ten.
		Returns the result of adding the two arguments as a word. 
	'''
	# Set the agrument error to None because initally, we don't have an error.
	argument_error = None
	
	# Tuple containing words from zero to twenty.
	words = (
		'zero',
		'one',
		'two',
		'three',
		'four',
		'five',
		'six',
		'seven',
		'eight',
		'nine',
		'ten',
		'eleven',
		'twelve',
		'thirteen',
		'fourteen',
		'fifteen',
		'sixteen',
		'seventeen',
		'eighteen',
		'nineteen',
		'twenty'
		)
		
	try:
		# Verify both arguments are strings.
		if not isinstance(first_num, str) and not isinstance(second_num, str):
			raise AttributeError
		
		# Verify first argument is a string. 
		if not isinstance(first_num, str):
			argument_error = "first"
			raise AttributeError
		
		# Verify second argument is a string.
		if not isinstance(second_num, str):
			argument_error = "second"
			raise AttributeError
		
		# Since both arguments are strings, convert them to lower case.
		first_num = first_num.lower()
		second_num = second_num.lower()
		
		# Verify both arguments are between zero and ten.	
		if first_num not in words[:11] and second_num not in words[:11]:
			raise ValueError
		
		# Verify first argument is a word between zero and ten.
		if first_num not in words[:11]:
			argument_error = "first"
			raise ValueError
		
		# Verify second argument is a word between zero and ten.
		if second_num not in words[:11]:
			argument_error = "second"
			raise ValueError
		
		# Add the two values (indexes) together and return the result as a word. 
		value = words.index(first_num) + words.index(second_num)
		return words[value]
	
	# Handle the arguments that are not strings.
	except AttributeError:
		
		# Return which argument was not a string.
		if argument_error is not None:
			return "ERROR: The " + argument_error + " argument is not a string."
		
		# Return that both arguments are not strings.
		else:
			return "ERROR: Both arguments are not strings."
	
	# Handle the arguments that are not a word between zero and ten.
	except ValueError:
		
		# Return which argument was not a valid word.
		if argument_error is not None:
			return "ERROR: The " + argument_error + " argument did not use a word between zero and ten."
			
		# Return that both arguments are not valid words.
		else:
			return "ERROR: Both arguments did not use a word between zero and ten"
