"""EX03 - Structured Wordle."""

__author__ = "730388479"


def contains_char(search_string: str, search_char: str) -> bool:
    """Searches for single character in string."""
    assert len(search_char) == 1
    alt_indices: int = 0
    while alt_indices < len(search_string):
        if search_string[alt_indices] == search_char:
            return True
        else:
            alt_indices += 1 
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Given a guess word, returns codifed emoji string comparing to the secret word."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_string: str = ""
    while i < len(secret_word):
        if secret_word[i] == guess_word[i]:
            emoji_string += GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[i]):
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX
        i += 1
    return emoji_string 


def input_guess(expt_len: int) -> str:
    """Given an integer of the length of the secret word, prompts that length guess."""
    guess_word: str = str(input(f"Enter a {expt_len} character word: "))
    while len(guess_word) != expt_len:
        guess_word = input(f"That wasn't {expt_len} chars Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    guess_correct: bool = False
    while turn <= 6 and not guess_correct:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            guess_correct = True
        else:
            turn += 1
    if guess_correct:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()