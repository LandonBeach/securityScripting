# Guessing Game
# Author: Landon Beach
# Date: 2/13/17

# Import the integer RNG
from random import randint

# Greet the user.
print("Welcome to the Guessing Game!")
print("Press Ctrl-c to quit at any time.")

# An exception to handle invalid max values.
class invalidMax(Exception):
	pass

# Main loop of the game.
b = True
number = None
while b:
	try:
		# Prompt the user for a max ranger value.
		max = int(input("\nPlease enter a max range greater than 1: "))

		# If user enters an invalid max range, thrown an exception to handle it.
		if max <= 1:
			raise invalidMax()

		# Generate a random integer.
		number = randint(1,max)
		guessed = False
		guess_count = 0
		
		# Loops until user guesses correctly or give up.
		while not guessed:

			# Increment the number of guesses.
			guess_count += 1
			try:
				# Prompt the user every 15 guesses if they want to give up.
				# Loops until the user enters 'y' or 'n'
				# If the user enters 'y' then raise two KeyboardInterrupts to quit.
				while guess_count % 15 == 0:
					give_up = input("Give up (y/n)? ")
					if give_up.lower() == 'y':
						raise KeyboardInterrupt()
					elif give_up.lower() == 'n':
						break
					else:
						print("Invalid input.")

				# Prompt user to make a guess.
				# Tell the user if it is too high or too low.
				guess = int(input("\nPlease make a guess: "))
				if guess < number:
					print("Your guess is too low.")
				elif guess > number:
					print("Your guess is too high.")
				else:
					guessed = True

			# User didn't enter a valid integer.
			except ValueError:
				print("You didn't enter a valid integer.")

			# User gave us an EOF character.
			except EOFError:
				print("I found an EOF character. Please try again.")

			# User gave up. Raise another KeyboardInterrupt to quit game.
			except KeyboardInterrupt:
				raise KeyboardInterrupt()

			# Handle all other interrupts.
			except:
				print("I knew you would do that... Please try again.")

		# Congratulate the user for winning.
		print("\nCongratulations! You WON!!")

		# Grammar check! 
		# Tell the user how many guesses it took them.
		if guess_count == 1:
			print("It took you %d guess." % guess_count)
		else:
			print("It took you %d guesses." % guess_count)

		# Prompt the user if they want to play again.
		# Keep looping until the user enters 'y' or 'n'.
		play_again = True
		while play_again: 
			again = input("Play again (y/n)? ")

			# User want to keep playing.
			if again.lower() == 'y':
				play_again = False

			# User wants to quit. Thank them for playing and exit the game.
			elif again.lower() == 'n':
				print("Thank you for playing")
				b = False
				play_again = False

			# Handle invalid input from the user.
			else:
				print("Invalid input.")	

	# User entered an invalid max value. (e.g. max < 1)
	except invalidMax:
		print("You entered an invalid max value.")

	# User didn't enter an integer.
	except ValueError:
		print("You didn't enter an integer.")

	# User decided to quit.
	except KeyboardInterrupt:
		# Tell the user the number if it existed.
		if number is not None:
			print("\nThe number was %d" % number)
		
		# Thank the user and exit the main loop. (quit the game.)
		print("Thank you for playing")
		b = False 

	# Handle the EOF character.
	except EOFError:
		print("I found an EOF character. Please try again.")
	
	# Handle all the other interrupts.
	except:
		print("\nI knew you would do that... Please try again.")

