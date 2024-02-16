# Password Generator
Randomly generate a password.

## Requirements
For this challenge, write a script to do the following:

- Prompt the user for the desired length of the password to generate
- Prompt the user if they'd like their password to include special characters (!, @, #, $, %, &)
    - If yes, generate a password of the specified length including numbers, letters, and special characters
    - If no, generate a password of the specified length including only numbers and letters
- Prompt the user to press ENTER to generate another password

This process should repeat until the user stops the script with CTRL+C. \
Your script should also include error handling, you never know what the user will do, and how your code will react.

When you're done, compare your code to [mine](passwordGenerator.py). \
Assess what you did well, and what you could do better.

## Resources
I can't stop you from just Googling how to do this, but that won't help you learn!

[W3 Schools](https://www.w3schools.com/python/default.asp) is a great resource for almost any programming language.

## Tips, tricks, and best practices
1. If you find yourself repeating code, define a function for it.
2. Avoid putting if statements inside of other if statements, never nest!
3. If you get stuck, take a step back. Try to list in order the steps your script should follow, and go from there.
