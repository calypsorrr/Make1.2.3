#!/usr/bin/env python
"""
Een re-make van je rekenmachine die voldoet aan flowcontrol.
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


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


def main():
    global x
    global y
    x = input("Give me a Number user ")  # Asking the user for a number
    y = input("Give me a second number user ")  # Asking the user for a number

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

    restart = input("Do you want to start again? if so type 'yes' else type 'no' ").lower()
    if restart == "yes":
        print('\n' * 80)
        main()
    else:
        exit()

if __name__ == '__main__':  # code to execute if called from command-line
    main()
