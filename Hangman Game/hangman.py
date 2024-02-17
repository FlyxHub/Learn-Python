import os, random # Import modules

def clear(): # Clears the terminal
    os.system('cls')
    return

def pause(): # Makes the user press ENTER to continue
    input('Press ENTER to continue.')
    return

words = ['crane', 'swamp', 'crash', 'soupy', 'quart', 'shart'] # Defines pool of words

def pickWord(): # Chooses a word from the list, and splits it into list of letters
    word = random.choice(words)
    wordSplit = list(word)
    return wordSplit
    
def updateList(list:list, index:int, letter:str): # Updates list 
    list[index] = letter
    return list

def newGuess(): # Asks user for guess
    guess = input('Guess a letter: ').lower()
    return guess

# -------------------- Game Loop -------------------- #
while True: # Plays the game until the user CTRL+C's
    victory = False
    wordList = pickWord()
    guessList = ['_', '_', '_', '_', '_']

    while victory == False:
        clear()
        print(' '.join(guessList))

        guess = newGuess()
        if guess in wordList:
            updateList(guessList, wordList.index(guess), guess)
        else:
            print('Try again!')
            pause()

        if ''.join(guessList) == ''.join(wordList):
            victory = True
        else:
            pass

    clear()
    print(f"The word was {''.join(wordList).upper()}. You win!")
    pause()

# Code currently does not support words with duplicate letters. May or may not update later.
    
