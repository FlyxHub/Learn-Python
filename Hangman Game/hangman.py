import os # Import modules
from random_word import RandomWords


def clear():  # Clears the terminal
    os.system("cls")
    return


def pause():  # Makes the user press ENTER to continue
    input("Press ENTER to continue.")
    return


def pickWord():  # Chooses a word from the list, and splits it into list of letters\
    word = RandomWords().get_random_word()
    wordSplit = list(word)
    return wordSplit


def initializeList(wordList: list):  # Initializes the blank list
    blankList = []
    for letter in list(wordList):
        blankList.append("_")
    return blankList


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
    guessList = initializeList(wordList)

    while victory == False:
        clear()
        print(" ".join(guessList))

        guess = newGuess()
        repeats = findRepeats(wordList, guess)
        if guess in wordList:
            for index in repeats:
                updateList(guessList, index, guess)
        else:
            pass

        if "".join(guessList) == "".join(wordList):
            victory = True
        else:
            pass

    clear()
    print(f"The word was {''.join(wordList).upper()}. You win!")
    pause()
