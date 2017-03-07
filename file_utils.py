def file_io(file_name, mode, *text):
	mode = mode.lower()
	# Open the file
	with open(file_name) as f:
		# Use the mode to determine how to handle the file.
		if (mode == 'r'):
			# Print the contents to stdout.
			pass
		elif (mode == 'r+'):
			# Determine if the user sent a list of strings to write.
			# If the user sent lines to write, write the lines (each on a new line)
			# If not, read the lines of the file and print them to stdout.
			pass
		elif (mode == 'a' or mode == 'w'):
			# Write each string to a new line in the file.
			pass
		else:
			# Invalid mode
			pass

