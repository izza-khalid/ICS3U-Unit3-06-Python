#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program checks if the number you chose matches
# with user input

import random
some_variable = random.randint(1, 100)
# a number between 1 and 100


def main():
    # This function checks if the number you chose matches

    # input
    print("Quick! Pick a number between 0 and 100")
    print("")
    integer_as_string = input("Enter the number of your choice: ")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        print("You entered an integer correctly")
        print("")
        if integer_as_number == some_variable:
            print("You got it right")
        else:
            print("Better luck next time")
            print("The random number was", some_variable, ".")
    except Exception:
        print("This was not an integer")
    finally:
        print("")
        print("Lets try again!!!")


if __name__ == "__main__":
    main()
