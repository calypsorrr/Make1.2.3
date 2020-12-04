#!/usr/bin/env python
"""
Info about our project comes here
"""


# Imports
import random
import string


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


# My function to generate lower cases as much as the user want to
def lower_cases():
   global result_1
   user_1 = int(input("How many lower cases do you want in your password? "))
   chars_small = string.ascii_lowercase
   result_1 = ''.join(random.choice(chars_small) for i in range (user_1))


# My function to generate upper cases as much as the user want to
def upper_cases():
   global result_2
   user_2 = int(input("How many upper cases do you want in your password? "))
   chars_upper = string.ascii_uppercase
   result_2 = ''.join(random.choice(chars_upper) for i in range(user_2))


# My function to generate digits as much as the user want to
def digitals():
   global result_3
   user_3 = int(input("How many digits do you want in your password? "))
   digits = string.digits
   result_3 = ''.join(random.choice(digits) for i in range(user_3))

def charaters():
   global result_4
   user_4 = int(input("How many charaters do you want in your password? "))
   charaters_1 = string.punctuation
   result_4 = ''.join(random.choice(charaters_1) for i in range(user_4))

# A function to randomise the string i already have from the input of the user
def random_string():
   global  result_5
   result_5 = ''.join(random.sample(result_1 + result_2 + result_3 + result_4, len(result_1 + result_2 + result_3 +
                                                                                   result_4)))

def restart():
   # Asking the user if he want to end it here or want to go again
   restart = input("Do you want to start again? if so type 'yes' else type 'no' ").lower()
   if restart == "yes":
      print('\n'*80)
      main()
   else:
      exit()


# My main fucntion where all the other functions are
def main():
   lower_cases()
   upper_cases()
   digitals()
   charaters()
   random_string()

   print(result_5)

   print("\n")

   restart()

if __name__ == '__main__':  # code to execute if called from command-line
    main()