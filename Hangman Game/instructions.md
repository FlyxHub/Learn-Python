# Hangman (WIP)
Guess the letters in the mystery word!

## Requirements
For this challenge, write a script to do the following:

- Randomly choose a word from a list of words
- Display a line of blank spaces, coresponding to the letters in the word
- Prompt the user to enter a letter
    - If the letter is in the word, replace the blank space with the letter
    - If the letter is not in the word, prompt the user to try again
- Display a "You win!" message when all of the letters have been guessed
- Prompt the user to press ENTER to play again

This process should repeat until the user stops the script with CTRL+C. \
Your script should also include error handling, you never know what the user will do, and how your code will react.

When you're done, compare your code to [mine](hangman.py). \
Assess what you did well, and what you could do better.

## Resources
I can't stop you from just Googling how to do this, but that won't help you learn!

[W3 Schools](https://www.w3schools.com/python/default.asp) is a great resource for almost any programming language.

## Tips, tricks, and best practices
1. If you find yourself repeating code, define a function for it.
2. Avoid putting if statements inside of other if statements, never nest!
3. If you get stuck, take a step back. Try to list in order the steps your script should follow, and go from there.
4. Command line scripts look best in an empty terminal, clear it!
