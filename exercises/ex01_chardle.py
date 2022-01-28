"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730388479"

five_character_word: str = str(input("Enter a 5-character word: "))
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = str(input("Enter a single character: "))
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
count: int = 0

print("Searching for " + single_character + " in " + five_character_word)

if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    count = count + 1
if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    count = count + 1
if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    count = count + 1
if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    count = count + 1
if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
else:
    if count == 1:
        print(str(count) + " instance of " + single_character + " found in " + five_character_word)
    else:
        print(str(count) + " instances of " + single_character + " found in " + five_character_word)