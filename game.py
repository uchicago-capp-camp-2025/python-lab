import random

words = [
    "air",
    "boo",
    "cat",
    "cow",
    "dad",
    "dog",
    "elf",
    "fox",
    "hey",
    "mom",
    "oil",
    "pig",
    "rye",
]


def main():
    # guesses remaining
    guesses = 3
    # letters that have been revealed (all empty at first)
    revealed = ["_", "_", "_"]
    guessed = set()

    # pick a word at random
    #word = random.choice(words)
    word = words[0]

    while guesses > 0:
        print("\n-----------------------------")
        print("Word: ", " ".join(revealed))
        print("Letters Guessed: ", ", ".join(sorted(guessed)))
        print("Guesses Remaining: ", guesses)
        print()
        letter = input("Pick a letter: ")

        if letter in guessed:
            print(f"Already guessed {letter}!")
        else:
            # update status
            guessed.add(letter)
            guesses -= 1

            # check word one letter at a time
            for index, word_letter in enumerate(word):
                if letter == word_letter:
                    revealed[index] = letter

            # if revealed is all letters, the player has won!
            if "_" not in revealed:
                print(f"{word}! You Win!")
    print(f"Sorry! The word was {word}")


if __name__ == "__main__":
    main()
