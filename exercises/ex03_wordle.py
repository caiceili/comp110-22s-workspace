"""EX03 - Wordle."""

__author__ = "730406845"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret_word: str = "codes"  # the secret word being guessed
    guess_word: str = ""  # the word entered by the user
    playing: bool = True  # a variable to show that user is playing
    # this loop will run while the user's number of turns is below 6 and the bool variable playing is true. 
    while turns <= 6 and playing:
        print(f"=== Turn {turns}/6 ==== ")
        guess_word = input_guess(len(secret_word))  # gives us the length of the secret word to plug into guess word as an argument as our expected length
        print(emojified(guess_word, secret_word))  # gives us the arguments to plug into emojified
        if guess_word == secret_word:  # if user guesses the correct secret worrd, we tell them so on this guess and we do not need to repeat 
            print(f"You won in {turns}/6 turns! ")
            playing = False
        if guess_word != secret_word and turns == 6:  # if user guesses incorrectly for secret word, we tell them so
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1
    

def contains_char(guess_word: str, char: str) -> bool: 
    """Checks for guess_character anywhere in guess_word."""
    assert len(char) == 1  # length fo character will be 1 
    idx = 0  # initialize at zero so we can move guess word character by character
    contains_char = False
# this loop will move through guesss word character by character to check if guess char is anywhere 
# in guess_word until the value of index is the same as the length of guess word 
    while idx < len(guess_word):
        if char == guess_word[idx]:
            contains_char = True
        idx += 1
    return contains_char


def emojified(guess_word: str, secret_word: str) -> str: 
    """Given two strings of the same length, returns a string of emoji whose color codifies results of contains char."""
    assert len(guess_word) == len(secret_word)
    emojified = "" 
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx = 0 
# this loop will assign and concatenate emojis depending on whether characters are in the same space in the guess word 
# and secret word, exist some place within the gues word and secret word, or do not exist in the secret word at all. 
# The loop uses contains_char to seaarch for the need of a yellow emojii.
    while idx < len(secret_word):
        if guess_word[idx] == secret_word[idx]:
            emojified += GREEN_BOX
        elif contains_char(secret_word, guess_word[idx]): 
            emojified += YELLOW_BOX
        else:
            emojified += WHITE_BOX
        idx += 1 
    return emojified


def input_guess(expected_length: int) -> str: 
    """Given an integer expected_length, prompts the user for a guess and continues prompting until user provides a guess of the expected length."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")  # gets input of guess word by prompting for a word of a certain length
    # This loop makes sure that users are entering a word of the same length as the secret word and returns it for use by the main function.
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word


# allows program to run a a module and makes it possible for other modules to import and use this function
if __name__ == "__main__":
    main()