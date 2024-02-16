import os # Import modules

def clear(): # Clears the terminal
    os.system('cls')
    return

def add(num1:float, num2:float): # Adds the numbers
    return num1 + num2

def subtract(num1:float, num2:float): # Subtracts  the numbers
    return num1 - num2

def multiply(num1:float, num2:float): # Multiplies the numbers
    return num1 * num2

def divide(num1:float, num2:float): # Divides the numbers
    return num1 / num2

# -------------------- Program Start -------------------- #
clear()
equation = input('Enter your equation separated by spaces: \n')
equationList = equation.split(' ')

num1 = float(equationList[0])
num2 = float(equationList[2])
operation = equationList[1]

if operation == '+':
    answer = add(num1, num2)
    clear()
    print(f'{equation} = {answer}')
elif operation == '-':
    answer = subtract(num1, num2)
    clear()
    print(f'{equation} = {answer}')
elif operation == '*':
    answer = multiply(num1, num2)
    clear()
    print(f'{equation} = {answer}')
elif operation == '/':
    answer = divide(num1, num2)
    clear()
    print(f'{equation} = {answer}')

