import os, random # Import modules

def clear(): # Clears the terminal
    os.system('cls')
    return

coin = ['heads', 'tails'] # Defines the coin

def flip(): # Flips the coin and returns outcome
    flip = random.choice(coin)
    return flip

def call(): # Gets the user's prediction
    userCall = input('Enter HEADS or TAILS: ').lower()
    return userCall

def check(flip:str, call:str): # Validates user's preduction and determines winner
    if call not in coin:
        return 'You must choost either HEADS or TAILS. Try again'
    elif call == flip:
        return f"It's {flip.upper()}. You win!"
    else:
        return f"It's {flip.upper()}. You lose."
    
# -------------------- Game Loop -------------------- #
while True: # Plays the game until the user CTRL+C's
    clear()
    coinFlip, userCall = flip(), call()
    print(check(coinFlip, userCall))
    input('Press ENTER to play again.')

