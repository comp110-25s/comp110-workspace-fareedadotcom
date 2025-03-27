"""ex02 uses multiple little functions to make a wordle"""

__author__: str = "730561781"


def contains_char(search_in: str, search_for: str) -> bool:
    """Looks for a given character in another string"""
    assert len(search_for) == 1, f"len('{search_for}') is not 1"
    x: int = 0
    while x < len(search_in):
        if search_for == search_in[x]:
            return True
        else:
            x += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojifies the guess/secret word match in coloured boxes"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    accuracy: str = ""
    x: int = 0
    while x < len(secret):
        if not contains_char(secret, guess[x]):
            accuracy += WHITE_BOX
        else:
            if guess[x] == secret[x]:
                accuracy += GREEN_BOX
            else:
                accuracy += YELLOW_BOX
        x += 1
    return accuracy


def input_guess(expected_length: int) -> str:
    """Makes sure the word length of the guess is correct"""
    guessed: str = input(f"Enter a {expected_length} character word:")
    while len(guessed) != expected_length:
        guessed = input(f"That wasn't {expected_length} chars! Try again:")
    return guessed


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    they_win: bool = False
    while turn <= 6 and not they_win:
        print(f"=== Turn {turn}/6 ===")
        guessed = input_guess(len(secret))
        print(emojified(secret, guessed))
        if guessed == secret:
            they_win = True
        else:
            turn += 1
    if they_win:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
