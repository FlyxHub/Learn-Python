import os, random  # Import modules


def clear():  # Clears the terminal
    os.system("cls")
    return


def pause():  # Makes the user press ENTER to continue
    input("Press ENTER to continue.")
    return


words = [
    "crane",
    "swamp",
    "crash",
    "soupy",
    "quart",
    "shart",
    "stoop",
    "snoop",
    "creep",
]  # Defines pool of words


def pickWord():  # Chooses a word from the list, and splits it into list of letters
    word = random.choice(words)
    wordSplit = list(word)
    return wordSplit


def updateList(list: list, index: int, letter: str):  # Updates list
    list[index] = letter
    return list


def newGuess():  # Asks user for guess
    guess = input("Guess a letter: ").lower()
    return guess


def findRepeats(list: list, item: str):  # Finds indexes of repeat items in list
    repeats = []
    index = 0
    for letter in list:
        if letter == item:
            repeats.append(index)
        else:
            pass
        index += 1
    return repeats


# -------------------- Game Loop -------------------- #
while True:  # Plays the game until the user CTRL+C's
    victory = False
    wordList = pickWord()
    guessList = ["_", "_", "_", "_", "_"]

    while victory == False:
        clear()
        print(" ".join(guessList))

        guess = newGuess()
        repeats = findRepeats(wordList, guess)
        if guess in wordList:
            for index in repeats:
                updateList(guessList, index, guess)
        else:
            print("Try again!")
            pause()

        if "".join(guessList) == "".join(wordList):
            victory = True
        else:
            pass

    clear()
    print(f"The word was {''.join(wordList).upper()}. You win!")
    pause()

# Code currently only supports 5 letter words. May come back and fix later.
