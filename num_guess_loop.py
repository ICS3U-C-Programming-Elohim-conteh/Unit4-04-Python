#!/usr/bin/env python3
# Created by: Elohim Conteh
# Created on: Nov 18, 2026
# This program asks the user to guess a random number between 0 and 9
# and uses a break statement to exit the loop when they guess correctly.

import random


def main():
    # this function uses a break statement
    random_number = random.randint(0, 9)

    while True:
        # input
        user_guess_str = input("Enter a number between 0 and 9: ")

        # process & output
        try:
            user_guess_int = int(user_guess_str)
            if user_guess_int < 0 or user_guess_int > 9:
                print("{0} is not between 0 and 9.".format(user_guess_int))
            else:
                if user_guess_int == random_number:
                    print("You guessed correctly!")
                    break
                else:
                    print("You guessed wrong!")
        except Exception:
            print("{0} is not an integer.".format(user_guess_str))

    print("Done.")


if __name__ == "__main__":
    main()
