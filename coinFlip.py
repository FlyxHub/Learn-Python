import os, random # Import modules

coin = ['heads', 'tails'] # Defines the coin

def cls(): # Clears the terminal
    os.system('cls')
    return

def flip(): # Flips the coin and returns outcome
    flip = random.choice(coin)
    return flip

def call(): # Gets the user's prediction
    userCall = input('Enter HEADS or Tails: ').lower()
    return userCall

def check(flip:str, call:str): # Validates user's preduction and determines winner
    if call not in coin:
        return 'You must choost either HEADS or TAILS. Try again'
    elif call == flip:
        return f"It's {flip.upper()}. You win!"
    else:
        return f"It's {flip.upper()}. You lose."
    
while True: # Play the game until the user CTRL+C's
    cls()
    coinFlip, userCall = flip(), call()
    print(check(coinFlip, userCall))
    input('Press ENTER to play again.')

