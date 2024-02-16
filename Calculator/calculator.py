import os  # Import modules


def clear():  # Clears the terminal
    os.system("cls")
    return

# -------------------- Program Loop -------------------- #
while True:
    clear()
    equation = input("Enter your equation separated by spaces: \n")
    equationList = equation.split(" ")

    try:
        num1 = float(equationList[0])
        num2 = float(equationList[2])
        operation = equationList[1]
        calculatable = True
    except:
        clear()
        print("Failed to parse equation. Did you separate it with spaces?")

    if len(equationList) != 3:
        clear()
        print("Failed to perform calaulation. Make sure you only supply 2 numbers and one operation(2 + 2).")
        calculatable = False
    else:
        pass

    while calculatable is True:
        if operation == "^":
            answer = num1**num2
            clear()
            print(f"{equation} = {answer}")
            break
        elif operation == "+":
            answer = num1 + num2
            clear()
            print(f"{equation} = {answer}")
            break
        elif operation == "-":
            answer = num1 - num2
            clear()
            print(f"{equation} = {answer}")
            break
        elif operation == "*":
            answer = num1 - num2
            clear()
            print(f"{equation} = {answer}")
            break
        elif operation == "/":
            answer = num1 / num2
            clear()
            print(f"{equation} = {answer}")
            break
        else:
            clear()
            print(
                f'Unsupported operator "{operation}". Supported operators are ^, +, -, *, and /'
            )
            break

    input("Press ENTER to perform another calculation. ")
    calculatable = False
