#!/usr/bin/env python
"""
Info about our project comes here
"""

# imports
import json
import random
import datetime
from statistics import mean


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


# Varibles
global a
global date_time
global average
list_20 = random.sample(range(1, 400), 20)
date_time = ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
average = 'Average:', mean(list_20)


def use_write():
    with open('test.txt', 'a') as f:                  # writing all my data to test.txt
        f.write(json.dumps(list_20) + "\n")
        f.write(json.dumps(date_time) + "\n")
        f.write(json.dumps(average) + "\n")


def use_read():
    with open("test.txt") as f:                       # reading everything from test.txt
        for line in f:                                # this can be modified to show specifics from the test.txt
            print(line)

def restart():
    # Asking the user if he want to end it here or want to go again
    restart = input("Do you want to start again? if so type 'yes' else type 'no' ").lower()

    if restart == "yes":
        print('\n' * 80)
        main()
    else:
        exit()


# This is just the logic of the machine, my main function
def main():
    print("Which action do you want to preform? ")

    print("1. Write")
    print("2. Read")

    input_user = input()

    if input_user == "1":
        use_write()

    if input_user == "2":
        use_read()

    restart()

if __name__ == '__main__':  # code to execute if called from command-line
    main()