"""EX02 One Shot Wordle."""

__author__ = "730406845"

secret_word: str = "python"
entered_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
emoji: str = ""
idx: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(entered_word) != len(secret_word):
    print(f"That was not {len(secret_word)} letters! ")
    entered_word = input("Try again: ")

while idx < len(secret_word):
    if entered_word[idx] == secret_word[idx]:
        emoji += GREEN_BOX
    else:
        guessed_character: bool = False
        alt_idx: int = 0
        while not guessed_character and alt_idx < len(secret_word):
            if entered_word[idx] == secret_word[alt_idx]:
                guessed_character = True
            alt_idx += 1
        if guessed_character:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX 
    idx += 1

print(emoji)

if entered_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")