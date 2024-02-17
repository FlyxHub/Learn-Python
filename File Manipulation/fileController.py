import os  # Import modules

dir = os.path.dirname(__file__)  # Save directory of script


def clear():  # Clears the terminal
    os.system("cls")
    return


def pause():  # Makes the user press ENTER to continue
    input("Press ENTER to continue.\n")
    return


def updateFile(fileName: str, text: str = None):  # Creates/opens file and optionally writes text to it
    if not text:
        try:
            file = open(f"{dir}/{fileName}", "x")
        except FileExistsError:
            exitCode = f'File "{fileName}" already exists. Try writing text to it.'
            return exitCode
        except PermissionError:
            exitCode = "PERMISSION ERROR: Missing permissions to perform action, verify file name and try again."
            return exitCode
        except Exception as exitCode:
            return exitCode
        else:
            file.close()
            return None
    else:
        try:
            with open(f"{dir}/{fileName}", "a") as file:
                file.write(f"{text.strip()}\n")
        except PermissionError:
            exitCode = "PERMISSION ERROR: Missing permissions to perform action, verify file name and try again."
            return exitCode
        except Exception as exitCode:
            return exitCode
        else:
            file.close()
            return None


menu = """
Select an number from the menu.
--------------------------------
1. Create an empty file
2. Write to file (create if not exists)
3. Exit
--------------------------------
Enter your selection here: 
"""


# -------------------- Program Loop -------------------- #
while True:
    exitCode = 1
    clear()
    selection = input(menu)
    if selection == "1":
        clear()
        fileName = input("Enter your desired file name (including extension): ").strip()
        exitCode = updateFile(fileName)
    elif selection == "2":
        clear()
        fileName = input("Enter your desired file name (including extension): ").strip()
        text = input("Enter text to write to the file: ")
        exitCode = updateFile(fileName, text)
    elif selection == "3":
        clear()
        print("As you wish. Stopping script...")
        break
    else:
        clear()
        print("Invalid selection. Please select a number from the menu.")
        pause()

    if not exitCode:
        clear()
        print("Great success!")
        pause()
    elif exitCode == 1:
        pass
    else:
        clear()
        print(exitCode)
        pause()
