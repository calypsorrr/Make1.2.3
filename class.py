#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


class liedje(object):            # a class with a list named tekst
    def __init__(self, tekst):
        self.tekst = tekst

    def zingen(self):            # this will put every sentence on its own line
        for x in self.tekst:
            print(x)



def birthday():              # birthday song
    global verjaardagslied
    verjaardagslied = liedje(["Happy birthday to you", "Happy birthday to you", "Happy birthday dear Stijn",
                          "Happy birthday to you", "Een fijne verjaardag voor jou", "Een fijne verjaardag voor jou",
                          "Een fijne verjaardag",  "fijne verjaardag", "Een fijne verjaardag voor jou!"])
    verjaardagslied.zingen()

def chrismass():            # chrismass song
    kerstliedjes = liedje(["Have yourself a merry little Christmas", "Let your heart be light", "From now on",
                      "Our troubles will be out of sight", "Have yourself a merry little Christmas",
                      "Make the Yule-tide gay", "From now on", "Our troubles will be miles away",
                      "Here we are as in olden days", "Happy golden days of yore", "Faithful friends who are dear to us",
                      "Gather near to us once more", "Through the years we all will be together", "If the fates allow",
                      "Hang a shining star upon the highest bough", "And have yourself a merry little Christmas now",
                      "Here we are as in olden days", "Happy golden days of yore", "Faithfull friends who are dear to us",
                      "Gather near to us once more", "Through the years", "We all will be together", "If the fates allow",
                      "So hang a shining star upon the highest bough", "And have yourself a merry little Christmas now"])
    kerstliedjes.zingen()

def restart():
    # Asking the user if he want to end it here or want to go again
    restart = input("Do you want to start again? if so type 'yes' else type 'no' ").lower()

    if restart == "yes":
        print('\n' * 80)
        main()
    else:
        exit()

# main function
def main():
    print("which song do you want to hear? ")
    print("\n")
    print("1. Verjaardagslied ")
    print("2. Kerstlied ")

    user_1 = input()

    if user_1 == "1":
        birthday()
        print("\n")

    elif user_1 == "2":
        chrismass()
        print("\n")

    restart()

if __name__ == '__main__':  # code to execute if called from command-line
    main()