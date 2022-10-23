"""
Created by Ruben Castillo
Language: Python
Overview: Python application is a guessing game where the user is trying to guess a random number. 
This application also demonstrates the use of linear search and binary search.
"""

import random

"""
#Task 1: Computer will generate a random number, then you will try to guess it
def guess_random_number(tries, start, stop):
    number = random.randrange(start, stop, 1)

#While loop is made such that as long as values does not equal 0 it will execute the code in the while loop.
    while tries != 0:
        print("Number of tries left:", tries)
        user = input("Guess a number between 0 and 10:")
        #converts the string input to inteteger to be used in the IF statement
        a = int(user)
        if a == number:
            print("You have guessed correctly, you win!")
            break
        elif a > number:
            print("Your guess is to high!")
        elif a < number:
            print("Your guess is to low!")
        # decrements the number of tries if the number guess does not equal the number.
        tries -= 1
    else:
        print("You have run out of tries, try again")

#values passed to the guess_random_number function (tries = 5, start = 0, stop=10)
guess_random_number(5, 0, 10)

"""


"""
#Task 2: Computer to generate random number, then the computer will try to guess it using linear search.
def guess_random_num_linear(tries, start, stop):
    num = random.randrange(start, stop, 1)
    print("The number for the program to guess is: ", num)
#For loop to execute the number throughout the range from the user.
    for x in range(start, tries, 1):
        comp_guess = random.randrange(start, stop,1)
        print("Number of tries left is: ", tries)
        print("The program is guessing ....", comp_guess)
        if comp_guess == num:
            print("The program has guessed the correct number, which is: ", comp_guess)
            break
        elif comp_guess != num:
            tries -= 1
            if tries == 0:
                print("The computer has not been able to guess the correct number")
                return

guess_random_num_linear(5, 0, 10)
"""


"""
#Task 3 Computer to generate a random number, then the computer will try to guess it using binary search.
def guess_random_num_binary(tries, start, stop):
    target = random.randrange(start, stop, 1)
    print("Random number to find: ", target)
    #lower bound is at index of 0
    lower_bound = start
    #upper bound is the highest index
    upper_bound = stop - 1
    for x in range(start, tries, 1):
        #pivot is the halfway poing between the lower and upper bound
        pivot = (lower_bound + upper_bound) // 2
        if pivot == target:
            print("found it!: ", pivot)
            break
        elif pivot > target:
            print("Guess higher")
            upper_bound = pivot - 1
            tries -= 1
            if tries == 0:
                print("Your program failed to find the number.")
                break
        elif pivot < target:
            print("Guess lower")
            lower_bound = pivot + 1
            tries -=1
            if tries == 0:
                print("Your program failed to find the number.")
                break

guess_random_num_binary(5, 0,100)
"""

