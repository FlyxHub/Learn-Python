import os, random # Import modules

def cls(): # Clears the terminal
    os.system('cls')
    return

def pause():
    input('Press ENTER to continue.')
    return

words = ['crane', 'swamp', 'crash'] # Defines pool of words

def pickWord(): # Chooses a word from the list, and splits it into list of letters
    word = random.choice(words)
    wordSplit = list(word)
    return wordSplit

def checkLetter(letter:str, list:list): # Checks if letter is in list
    if letter not in list:
        return 'Not present'
    else:
        return list.index(letter)

cls()  
wordList = pickWord()
word = ''.join(wordList)
print(word)
pause()
letter = input('Enter a letter: ')
checkResult = checkLetter(letter, wordList)
print(checkResult)

