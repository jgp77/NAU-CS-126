__author__='Joshua Pollock'
'''
Step 1:
    This problem is asking me to create a program to calculate how much
    money is spent on gas during a trip. I will be assuming the user will not
    input money symbols or gallon units, but will enter in correct info. I have
    all the information needed to solve the issue at hand.
Step 2:
    In this code I will be using simple algebraic functions, float commands,
    input commands, and return functions. This will be able to solve the
    constraints that are given to us and will create a functioning program
Step 3:
'''


def trip_cost():
    tank_size=float(input('What is the size of the gas tank? (in gallons) '))
    miles_per_tank=float(input('How many miles do you get per tank? '))
    cost_per_gallon=float(input('What is the cost of gas per gallon? '))
    number_of_miles=float(input('How many miles are you traveling? '))
    return ('$' + str((number_of_miles / miles_per_tank) *
                      tank_size * cost_per_gallon))
'''
Step 4:
    At first I had tried to use integers for the input commands.
    I decided that this would not work it someone had a decimal
    amount for gas tank size, partial miles, or cents in their gas price.
    I changed the integers to floats in order to prevent this from happening.
    I also cut down on some variable and just had all the math done in the
    return function. This simplified the lines of code needed. This code
    solves the issue at hand and provides a valid solution.
'''
