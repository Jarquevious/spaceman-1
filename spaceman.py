import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    with open('words.txt', 'r') as f:
        words_list = f.read().split(' ')

    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    return_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            return_word.append(letter)
        else:
            return_word.append('_')
    return ''.join(return_word)


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''

    for letter in secret_word:
        if letter == guess:
            return True

    return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    incorrect_guesses = 7

    print('Welcome to spaceman!')
    print('The secret word contains: {} letters'.format(len(secret_word)))
    print('You have {} incorrect guesses left, please enter one letter per round'.format(
        incorrect_guesses))
    # print('------------------------------')

    guessed_word = ""
    correct_guesses = []
    # while incorrect_guesses != 0:
    while True:
        # Print to make it easier to read where you are in the program
        print('------------------------------ \n')

        # Check to see if they have won the game before doing anything else
        if is_word_guessed(secret_word, correct_guesses):
            print("Congrats!  You have won the game!")
            break

        # Check to see if their incorrect guesses is at 0
        if incorrect_guesses == 0:
            print("You lost the game.. Sorry about that")
            print("The answer was: {}".format(secret_word))
            break

        # Get user input
        letter = input("Enter a letter: ")
        if is_guess_in_word(letter, secret_word):
            # Add the letter to the correct guesses
            correct_guesses.append(letter)
            # Get the new guessed word with the updated correct letters
            guessed_word = get_guessed_word(secret_word, correct_guesses)

            # Print information and where they are at in the game,
            print("Your guess appears in the word!")
            print("Guessed word so far:  {}".format(guessed_word))
        else:
            # Get the letters that they have so far.
            guessed_word = get_guessed_word(secret_word, correct_guesses)

            # Remove one off of the incorrect guess counter
            incorrect_guesses -= 1

            # Print information and where they are at in the game
            print("Sorry, your guess was not in the word, try again")
            print("You have {} incorrect guesses left".format(incorrect_guesses))
            print("Guessed word so far: {}".format(guessed_word))

    # TODO: check if the game has been won or lost


# These function calls that will start the game
# secret_word = 'banana'
# spaceman(secret_word)
secret_word = load_word()
spaceman(load_word())


def test():
    # secret_word = load_word()  # Get a random secret word
    get_guessed_word('hello', ['h', 'e', 'l'])  # Hell_
    is_word_guessed('hi', ['h', 'i'])  # True
    is_word_guessed('hi', ['h'])  # False

# test()
