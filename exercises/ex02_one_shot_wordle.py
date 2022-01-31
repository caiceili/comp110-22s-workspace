"""EX02 One Shot Wordle."""

__author__ = "730406845"

secret_word: str = "python"
entered_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
emoji: str = ""
idx: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Here I initialized variables for later use and collected the first input for 
# the entered word. I used an f string with the length of the secret word so 
# that the program still runs with a word of a different length than "python."
while len(entered_word) != len(secret_word):
    print(f"That was not {len(secret_word)} letters! ")
    entered_word = input("Try again: ")
# Here I created a while loop that will not move on until the user enters 
# a word that is the same length as my secret word.
while idx < len(secret_word):
    if entered_word[idx] == secret_word[idx]:
        emoji += GREEN_BOX
# If a character at some point in the entered word is the same character at 
# that same point in the secret word, add a green box. This will repeat as 
# idx increases by 1 until idx is not less than the length of the secet word 
# and the loop ends.
    else:
        guessed_character: bool = False
        alt_idx: int = 0
# initialized new variables to use within this while loop
        while not guessed_character and alt_idx < len(secret_word):
            if entered_word[idx] == secret_word[alt_idx]:
                guessed_character = True
            alt_idx += 1
        if guessed_character:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX 
    idx += 1
# f the characters aren't initially equal, the program will move to this loop. It will 
# check one character of the entered word against every character of 
# the secret word by adding 1 to alt_idx until the length is not less than secret word or 
# not not guessed character. If the characters are equal, then add a yellow box to indicate
# the character at this point in the entered word is somewhere in the secret word. 
# If the characters are not equal, add a white box to indicate the character is 
# nowhere in the secret word. Then the program adds 1 to idx and if the new idx value
# does not lead to a green box, it will go through the yellow/white box while loop.

print(emoji)
# Once the program goes through all of the characters of the secret word with the 
# appropriate while loops, the appropriate emojis will print.

if entered_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
# If the entire guessed word is the same as
# the entire secret word, the user has guessed correctly. 
# If not, they must use the information the program gave them to guess again.