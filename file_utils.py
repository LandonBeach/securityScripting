# Landon Beach
# 3/8/17

def file_io(file_name, mode, *text=None):
	mode = mode.lower()
	# Open the file
	with open(file_name, mode) as f:
		# Use the mode to determine how to handle the file.
		if mode == 'r':
			# Print the contents to stdout.
			print(f.read())
		elif mode == 'r+':
			# Determine if the user sent a list of strings to write.
			# If the user sent lines to write, write the lines (each on a new line)
			if text is not None:
				for t in text:
					f.write(t + "\n")
			# If not, read the lines of the file and print them to stdout.
			else:
				print(f.read())
		elif mode == 'a' or mode == 'w':
			# Write each string to a new line in the file.
			if text is not None:
				for t in text:
					f.write(t + "\n")
