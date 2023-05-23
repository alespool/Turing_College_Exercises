# For this exercise:
# Write a function (guessing_game) that takes no arguments.
#
# When run, the function chooses a random integer between 0 and 100 (inclusive).
#
# Then ask the user to guess what number has been chosen.
#
# Each time the user enters a guess, the program indicates one of the following:
#
# #Too high
#
# #Too low
#
# # Just right
# If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
# The program only exits after the user guesses correctly.

import random
# number = random.randint(0,100)


def guessing_game():
    num = random.randint(0, 100)

    i = 0

    while i <= 3:

        user_input = int(input("I chose a number between 0 and 100, make a guess: "))

        if user_input == num:
            print(f"You guessed it right! It's {num}")
            break

        elif user_input >= num:
            print(f"The number I had in mind is lower than {user_input}")
            print("Try again!")
            print()

        elif user_input <= num:
            print(f"The number I had in mind is higher than {user_input}")
            print("Try again!")
            print()

        i += 1
        if i == 3:
            print(f"Sorry, too many attempts!")
            break


guessing_game()
