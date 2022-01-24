"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730406845"

entered_word: str = input("Enter a 5-character word: ")
if len(entered_word) < 5:
    print("Error: Word must contain 5 characters. ")
    exit()
if len(entered_word) > 5:
    print("Error: Word must contain 5 characters. ")
    exit()

entered_character: str = input("Enter a single character: ")
if len(entered_character) > 1:
    print("Error: Character must be a single character. ")
    exit()
if len(entered_character) < 1:
    print("Error: Character must be a single character. ")
    exit()

instances_found: int = 0


print("Searching for " + entered_character + " in " + entered_word)

if entered_character == entered_word[0]:
    print(entered_character + " found at index 0 ")
    instances_found += 1
if entered_character == entered_word[1]:
    print(entered_character + " found at index 1 ")
    instances_found += 1
if entered_character == entered_word[2]:
    print(entered_character + " found at index 2 ")
    instances_found += 1
if entered_character == entered_word[3]:
    print(entered_character + " found at index 3 ")
    instances_found += 1
if entered_character == entered_word[4]:
    print(entered_character + " found at index 4 ")
    instances_found += 1

if instances_found == 0:
    print("No instances of " + entered_character + " found in " + entered_word)
if instances_found == 1: 
    print(str(instances_found) + " instance of " + entered_character + " found in " + entered_word)
if instances_found >= 2:
    print(str(instances_found) + " instances of " + entered_character + " found in " + entered_word)

