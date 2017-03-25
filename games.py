# Number Guessing Game
# Author: Landon Beach
# Date: 3/27/17

from random import randint

class Game():
    """ A base Game class that handles users/passwords and logging in. """
    def __init__(self):
        """ This method creates an instance of a Game object and
        reads credentials from a login file.
        """
        self.filename = "user_list.txt"
        self.file_exists = True
        self.logged_in = False
        creds = []
        try:
            # Read in all non-whitespace lines and put in a credential list.
            with open(self.filename, 'r') as f:
                for line in f:
                    if line.strip():
                        creds.append(line.strip())

        # Handle if the file does not exist.
        except FileNotFoundError:
            print('ERROR: The file "%s" does not exist.' % self.filename)
            self.file_exists = False

        # Split up the credentials into two lists: users and passwords.
        self.users = creds[0::2]
        self.passwords = creds[1::2]

    def login(self, user):
        """ This method takes a user as an string argument, asks for a
        password from stdin, and authenticates the given credentials
        against a login file.
        """
        # If the login file doesn't exists then return.
        self.logged_in = False
        if not self.file_exists:
            print('ERROR: The file "%s" does not exist' % self.filename)
            return

        # If the user argument is not a sring then return.
        if not isinstance(user, str):
            print("ERROR: Please pass a 'user' as a string argument.")
            return

        # If the user argument is an empty string then return.
        if not user.strip():
            print("ERROR: User must not be an empty string.")
            return

        try:
            # Retrieve the user's password from the login file
            # and remove any potential trailing whitespace.
            password = self.passwords[self.users.index(user)].strip()

            # Give the user three attempts to enter the correct password.
            password_attempts = 3
            while password_attempts > 0:
                password_attempts -= 1
                user_password = input("Please enter the password for %s: " % user)

                # The passwords match so the authentication was successful.
                if user_password.strip() == password:
                    self.logged_in = True
                    break
                # The authentication failed.
                else:
                    print("ERROR: Incorrect password!")

            if not self.logged_in:
                print("ERROR: Too many password attempts.")

        # Exit the login prompt if there is a keyboard interrupt.
        except KeyboardInterrupt:
            print("\nExiting...")

        # Handle the EOF character.
        except EOFError:
            print("\nExiting...")

        # The user does not exist.
        # Ask to create the user. If yes, it appends the user and
        # password to the login file.
        except ValueError:
            self.logged_in = False
            print('ERROR: The user "%s" does not exist.' % user)

            creating_user = True
            while creating_user:
                # Ask to create new user.
                create_user = input('Would you like to create user "%s" (y/n)? ' % user)

                # If yes, create a new user with a password.
                if create_user.lower() == 'y':
                    try:
                        invalid_password = True
                        while invalid_password:
                            user_password = input("Please enter a password: ")

                            # User entered a "valid" password.
                            if user_password.strip():
                                creating_user = False
                            # User entered a password with only white-space.
                            else:
                                print("ERROR: Password must not be empty.")

                    # If a keyboard interrupt occurs, then return.
                    except KeyboardInterrupt:
                        print("\nExiting...")
                        return

                    # Handle the EOF character.
                    except EOFError:
                        print("\nExiting...")
                        return

                    # Append the new user and password to the login file.
                    with open(self.filename, 'a') as f:
                        f.write(user)
                        f.write("\n")
                        f.write(user_password.strip())  # Remove trailing white-space.
                        f.write("\n")
                    self.logged_in = True
                    creating_user = False

                # If no, don't create the user and exit.
                elif create_user.lower() == 'n':
                    creating_user = False

                # Keep looping until we recieve valid input. (y/n)
                else:
                    print("ERROR: Invalid input.")

    def get_logged_in(self):
        """ Returns True if the login was successful, else returns false. """
        return self.logged_in

    def get_login_file(self):
        """ Returns the path of the login file as a string. """
        return self.file_name

    def set_login_file(self, filename):
        """ Set the path to the login file.
        The filename parameter must be a string.
        """
        if isinstance(filename, str):
            self.filename = filename


class NumberGame(Game):
    """ A number guessing game that inherits from the Game class.
    The user must successfully login before being able to play the game.
    """
    def __init__(self, user):
        """ This method creates a new instance of a NumberGame object.
        It reads from a login file for authentication. The default
        difficulty setting is 'easy'.
        """
        super().__init__()
        super().login(user)
        self.difficulty = 'easy'
        self.guess_range = 10

    def set_difficulty(self, difficulty):
        """ This method sets the difficult setting. The argument passed
        must be either 'easy', 'medium', or 'hard' as a string. Each
        setting increases the guessing range. The user must successfully
        login before being able to change the difficulty setting.
        """
        # If not logged in, then inform the user and return.
        if not super().get_logged_in():
            print("ERROR: Not logged in. Please login before setting the difficulty level.")
            return

        # If difficulty isn't a string, then inform the user and return.
        if not isinstance(difficulty, str):
            print("ERROR: Difficult setting must be a string.")
            return

        # Set the difficulty setting.
        difficulty = difficulty.lower()
        levels = {'easy': 10, 'medium': 100, 'hard': 1000}
        if difficulty in levels.keys():
            self.difficulty = difficulty
            self.guess_range = levels[difficulty]
        else:
            self.difficulty = None
            print("ERROR: Invalid difficulty setting.")
            print("ERROR: Difficulty setting must be 'easy', 'medium', or 'hard'.")

    def play(self):
        """ This method starts playing a new number game. The user must
        successfully login before being able to play.
        """
        # If they set an invalid difficulty setting then return.
        if self.difficulty is None:
            print("ERROR: Detected an invalid difficulty setting.")
            print("ERROR: Please set a vaild difficulty setting before playing.")
            return

        # If the user is logged in, then they can play the game.
        if super().get_logged_in():
            # Greet the user.
            print("\nWelcome to the Guessing Game!")
            print("The difficulty setting is set to '%s'." % self.difficulty)
            print("The range is from 1 to %d" % self.guess_range)
            print("Press Ctrl-c to quit at any time.")
            self.__game()
        else:
            print("ERROR: Not logged in. Please login before playing.")

    def __game(self):
        """ This is a private method that contains the actual Number
        Guessing game.
        """
        playing = True
        while playing:
            try:
                # Generate a random integer.
                number = randint(1, self.guess_range)
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
                            try:
                                give_up = input("Give up (y/n)? ")
                                if give_up.lower() == 'y':
                                    raise KeyboardInterrupt()
                                elif give_up.lower() == 'n':
                                    break
                                else:
                                    print("ERROR: Invalid input.")

                            # User gave us an EOF character.
                            except EOFError:
                                print("\nERROR: I found an EOF character. Please try again.")

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
                        print("ERROR: You didn't enter a valid integer.")

                    # User gave us an EOF character.
                    except EOFError:
                        print("\nERROR: I found an EOF character. Please try again.")

                    # User gave up. Raise another KeyboardInterrupt to quit game.
                    except KeyboardInterrupt:
                        raise KeyboardInterrupt()

                    # Handle all other interrupts.
                    except:
                        print("ERROR: I knew you would do that... Please try again.")

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
                    try:
                        again = input("Play again (y/n)? ")

                        # User want to keep playing.
                        if again.lower() == 'y':
                            play_again = False

                        # User wants to quit. Thank them for playing and exit the game.
                        elif again.lower() == 'n':
                            print("Thank you for playing!")
                            playing = False
                            play_again = False

                        # Handle invalid input from the user.
                        else:
                            print("ERROR: Invalid input.")

                    # User gave us an EOF character.
                    except EOFError:
                        print("\nERROR: I found an EOF character. Please try again.")

            # User didn't enter an integer.
            except ValueError:
                print("ERROR: You didn't enter an integer.")

            # User decided to quit.
            except KeyboardInterrupt:
                # Tell the user the number if it existed.
                if number is not None:
                    print("\nThe number was %d" % number)

                # Thank the user and exit the main loop. (quit the game.)
                print("Thank you for playing!")
                playing = False

            # User gave us an EOF character.
            except EOFError:
                print("\nERROR: I found an EOF character. Please try again.")

            # Handle all the other interrupts.
            except:
                print("\nERROR: I knew you would do that... Please try again.")
