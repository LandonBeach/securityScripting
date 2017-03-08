# Landon Beach
# 3/8/17

def file_io(file_name, mode, *text):
	''' This function handles file input/output. '''
	try:
		# Open the file
		# Use the mode to determine how to handle the file.
		with open(file_name, mode) as f:
			
			if mode == 'r':
				# Print the contents to stdout.
				print(f.read())
				
			elif mode == 'r+':
				# Determine if the user sent a list of strings to write.
				# If the user sent lines to write, write the lines (each on a new line).
				if len(text) > 0:
					for t in text:
						f.write(t)
						f.write('\n')
				# If not, read the lines of the file and print them to stdout.
				else:
					print(f.read())
			
			else:
				# Write/append each string to a new line in the file.
				if len(text) > 0:
					for t in text:
						f.write(t)
						f.write('\n')
				else:
					print("ERROR: No text to write.")
					
	# The file does not exist
	except FileNotFoundError:
		print("ERROR: File does not exist.")
	# The mode is invalid.
	except ValueError:
		print("ERROR: Invalid mode.")
	# The argument types are invalid.
	except:
		print("ERROR: All arguments must be strings.")
