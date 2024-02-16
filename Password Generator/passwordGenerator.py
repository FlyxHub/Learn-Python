import os, random, string # Import modules

letters = string.ascii_letters # Initialize list of letters
symbols = ['!', '@', '#', '$', '%', '&'] # Initialize list of symbols

def clear(): # Clears the terminal
    os.system('cls')
    return

def pause(): # Makes the user press ENTER to continue
    input('Press ENTER to continue.')
    return

def generatePassword(length:int, includeSymbols:bool): # Generates a random password
    passwordList = []

    if includeSymbols is False:
        for i in range(length):
            if random.randint(1, 2) == 1:
                passwordList.append(random.choice(letters))
            else:
                passwordList.append(str(random.randint(0, 9)))
        password = ''.join(passwordList)
        return password
    else:
        pass

    for i in range(length):
        roll = random.randint(1, 3)
        if roll == 1:
            passwordList.append(random.choice(letters))
        elif roll == 2:
            passwordList.append(str(random.randint(0, 9)))
        else:
            passwordList.append(random.choice(symbols))
    password = ''.join(passwordList)
    return password

# -------------------- Program Loop -------------------- #
while True: # Loops the program until the user CTRL+C's
    clear()
    clearToGenerate = False
    desiredLength = input('How many characters should your password contain? ')

    try:
        desiredLength = int(desiredLength)
        clearToGenerate = True
        proceed = True
    except:
        print(f'Failed to convert "{desiredLength}" to an integer. Try again with a whole number.')
        pause()
        clearToGenerate = False
        proceed = False

    if proceed is True:
        canIncludeSymbols = input('Can this password contain symbols? (y/n): ').lower()

        if canIncludeSymbols != 'y' and canIncludeSymbols != 'n':
            clearToGenerate = False
            print(f'Invalid option. Please try again.')
            pause()
        else:
            clearToGenerate = True
    else:
        pass

    while clearToGenerate is True:
        if canIncludeSymbols == 'y':
            generatedPassword = generatePassword(length=desiredLength, includeSymbols=True)
            clear()
            print(f"Your {desiredLength} character password is:\n{generatedPassword}")
            pause()
        elif canIncludeSymbols == 'n':
            generatedPassword = generatePassword(length=desiredLength, includeSymbols=False)
            clear()
            print(f"Your {desiredLength} character password is:\n{generatedPassword}")
            pause()
        else:
            print(f'Something went wrong. Please try again')
            pause()
        
        clearToGenerate = False

# So many nested if statements, so little time to de-nest
        
