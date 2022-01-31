"""EX02 One Shot Wordle."""

__author__ = "730406845"

secret_word: str = "python"
entered_word: str = input(f"What is your {len(secret_word)} guess? ")
emoji: str = ""
guessed_character: bool = False
i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(entered_word) != len(secret_word):
    print(f"That was not {len(secret_word)} letters! ")
    entered_word: str = input("Try again: ")

while i < len(secret_word):
    if entered_word[i] == secret_word[i]:
        emoji += GREEN_BOX
    else:
        j: int = 0
        while not guessed_character and j < len(secret_word):
            if entered_word[i] == secret_word[j]:
                guessed_character = True
            j += 1
        if guessed_character:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX 
    i += 1

print(emoji)

if entered_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")