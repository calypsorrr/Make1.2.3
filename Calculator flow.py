#!/usr/bin/env python
"""
Een re-make van je rekenmachine die voldoet aan flowcontrol.
"""

import time

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"

def use_x():
    global x
    try:
        x = int(input("Give me a Number user "))  # Asking the user for a number
    except ValueError as err:
        print(err)
        time.sleep(3)
        print("\n")
        use_x()

def use_y():
    global y
    try:
        y = int(input("Give me a second number user "))  # Asking the user for a number
    except ValueError as err:
        print(err)
        time.sleep(3)
        print("\n")
        use_y()

def numbers():
    global x
    global y
    try:
        x = int(input("Give me a Number user "))  # Asking the user for a number
        y = int(input("Give me a second number user "))  # Asking the user for a number
    except ValueError as err:
        print(err)
        time.sleep(3)
        print("\n")
        numbers()

def use_som():
    # ADD the numbers of the user
    print("The som of your numbers are " + str(int(x) + int(y)))
def use_subtract():
    # SUBTRACT the numbers of the user
    print("The subtraction of the numbers are " + str(int(x) - int(y)))

def use_multiplied():
    # MULTIPLY the numbers of the user
    print("The result of the numbers that where multiplied are " + str(int(x) * int(y)))

def use_divided():
    # DIVIDE the numbers of the user
    print("The result of the numbers that where divided is " + str(int(x) / int(y)))

def restart():
    # Asking the user if he want to end it here or want to go again
    print("\n")
    print("Do you want to continue with the same numbers or you want to put another in? ")
    print("1. change number 1")
    print("2. change number 2")
    print("3. change both numbers")
    print("4. continue with the same numbers")
    print("5. exit")

    restart = input()

    if restart == "1":
        main_x()
    elif restart == "2":
        main_y()
    elif restart == "3":
        main_both()
    elif restart == "4":
        main_same()
    else:
        exit()



def main_x():
    use_x()
    print("\n")

    print("now which calculation do you want to do?")  # Printing something out
    print("1. ADD")  # Printing 1. ADD
    print("2. SUBTRACT")  # Printing 2. SUBTRACT
    print("3. MULTIPLY")  # Printing 3. MULTIPLY
    print("4. DIVIDE")  # Printing 4. DIVIDE

    calculation = input()  # CALCULATION wil be a input from the user

    print("\n")

    if calculation == "1":  # If CALCULATION is 1 then do this
        use_som()

    elif calculation == "2":  # if CALCULATION is 2 then do this
        use_subtract()

    elif calculation == "3":  # if CALCULATION is 3 then do this
        use_multiplied()

    elif calculation == "4":  # If CALCULATION is 4 then do this
        use_divided()

    print("\n")

    restart()



def main_y():
    use_y()
    print("\n")

    print("now which calculation do you want to do?")  # Printing something out
    print("1. ADD")  # Printing 1. ADD
    print("2. SUBTRACT")  # Printing 2. SUBTRACT
    print("3. MULTIPLY")  # Printing 3. MULTIPLY
    print("4. DIVIDE")  # Printing 4. DIVIDE

    calculation = input()  # CALCULATION wil be a input from the user

    print("\n")

    if calculation == "1":  # If CALCULATION is 1 then do this
        use_som()

    elif calculation == "2":  # if CALCULATION is 2 then do this
        use_subtract()

    elif calculation == "3":  # if CALCULATION is 3 then do this
        use_multiplied()

    elif calculation == "4":  # If CALCULATION is 4 then do this
        use_divided()

    print("\n")

    restart()


def main_both():
    numbers()
    print("\n")

    print("now which calculation do you want to do?")  # Printing something out
    print("1. ADD")  # Printing 1. ADD
    print("2. SUBTRACT")  # Printing 2. SUBTRACT
    print("3. MULTIPLY")  # Printing 3. MULTIPLY
    print("4. DIVIDE")  # Printing 4. DIVIDE

    calculation = input()  # CALCULATION wil be a input from the user

    print("\n")

    if calculation == "1":  # If CALCULATION is 1 then do this
        use_som()

    elif calculation == "2":  # if CALCULATION is 2 then do this
        use_subtract()

    elif calculation == "3":  # if CALCULATION is 3 then do this
        use_multiplied()

    elif calculation == "4":  # If CALCULATION is 4 then do this
        use_divided()

    print("\n")

    restart()


def main_same():
    print("now which calculation do you want to do?")  # Printing something out
    print("1. ADD")  # Printing 1. ADD
    print("2. SUBTRACT")  # Printing 2. SUBTRACT
    print("3. MULTIPLY")  # Printing 3. MULTIPLY
    print("4. DIVIDE")  # Printing 4. DIVIDE

    calculation = input()  # CALCULATION wil be a input from the user

    print("\n")

    if calculation == "1":  # If CALCULATION is 1 then do this
        use_som()

    elif calculation == "2":  # if CALCULATION is 2 then do this
        use_subtract()

    elif calculation == "3":  # if CALCULATION is 3 then do this
        use_multiplied()

    elif calculation == "4":  # If CALCULATION is 4 then do this
        use_divided()

    print("\n")

    restart()

if __name__ == '__main__':  # code to execute if called from command-line
    main_both()
