"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730388479"

secret_word: str = "python"
len_secret_word: int = len(secret_word)
guess_word: str = str(input(f"What is your {len_secret_word}-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len_secret_word} letters! Try again: ")
    
i: int = 0
emoji_string: str = ""

while i < len_secret_word:
    if secret_word[i] == guess_word[i]:
        emoji_string += GREEN_BOX
    else:
        letter_in_secret_word: bool = False
        alternate_indices: int = 0
        while alternate_indices < len_secret_word and not letter_in_secret_word:
            if secret_word[alternate_indices] == guess_word[i]:
                letter_in_secret_word = True
            alternate_indices += 1
        if letter_in_secret_word == True:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
              
    i += 1

print(emoji_string)


if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
