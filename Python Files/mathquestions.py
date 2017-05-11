from random import randint
__author__='Lauryn Martin and Joshua  Pollock'
# Imports the randint function from random
correct=float(0)
# Sets correct to a float of 0
amount=int(input("How many questions will you answer? "))
# Asks user how many questions they want
difficulty=input('How hard do you want the problems? \n'
                   'Beginner, Intermediate, or Advanced? ').lower()
# Asks the user what difficulty they want
if difficulty == 'beginner':
    for i in range(amount):
        n1=randint(1, 8)
        n2=randint(1, 8)
        # Sets n1, n2, and n3 to a random integer between 1 and 8 and 1 and 0
        n3=randint(0, 1)
        # n3 i1s for deciding on what operation to give the user.
        # Ex: addition or subtraction
        if n3 == 1:
            prod=n1 + n2
            # Creates the prod variable as the correct solution
            ans=input('What is %d plus %d' % (n1, n2))
            # Asks the user the answer to a randomly generated problem
            if int(ans) == prod:
                print('That is right, well done.')
                correct += 1
                # If the user inputted answer matched,
                # prod then adds 1 to correct
            else:
                print("No, I'm afraid the answer is %d." % prod)
                # If the user inputes an incorrect,
                # answer displays the correct answer
        if n3 == 0:
            prod=n1 - n2
            ans=input('What is %d minus %d' % (n1, n2))
            if int(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
if difficulty == 'intermediate':
    for i in range(amount):
        n1=randint(1, 25)
        n2=randint(1, 25)
        n3=randint(0, 3)
        # Uses n1 and n2 in the range of 1 and 25 instead of 1 and 8
        # n3 now uses a random betweeen 0 and 3 for 4 problems
        if n3 == 1:
            prod=n1 + n2
            ans=input('What is %d plus %d' % (n1, n2))
            if int(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 0:
            prod=n1 - n2
            ans=input('What is %d minus %d' % (n1, n2))
            if int(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 2:
            prod=n1 * n2
            ans=input('What is %d times %d' % (n1, n2))
            if int(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 3:
            prod=float(n1 / n2)
            ans=input('What is %d divided by %d' % (n1, n2))
            if int(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
if difficulty == 'advanced':
    for i in range(amount):
        n1=randint(1, 25)
        n2=randint(1, 25)
        n3=randint(0, 4)
        # n1 and n2 remain the same as intermediate
        # n3 is now between 0 and 4 to give 5 random problems
        if n3 == 0:
            prod=3.14 * (n1**2)
            ans=input('What is the area of a circle with a radius \
                        of %d (Use 3.14 for pi)' % n1)
            if float(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 1:
            prod=n1**2
            ans=input('What is the area of a square \
                        with a side length of %d' % n1)
            if float(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 2:
            prod=n1 * n2
            ans=input('What is the area of a rectangle with %d as its base \
                        and %d as its height' % (n1, n2))
            if float(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 3:
            prod=3.14 * 2 * n1
            ans=input('What is the circumfrance of a circle with a radius \
                        of %d (Use 3.14 for pi)' % n1)
            if float(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
        if n3 == 4:
            prod=float(.5 * n1 * n2)
            ans=input('What is the area of a triangle with %d as its base \
                         and %d as its height' % (n1, n2))
            if float(ans) == prod:
                print('That is right, well done.')
                correct += 1
            else:
                print("No, I'm afraid the answer is %d." % prod)
if correct >= (amount/3) and correct >= (amount*2/3):
    print('Well Done!')
    # If the amount correct is greater than 1/3 and 2/3 of the total amount
elif correct >= (amount/3) and correct <= (amount*2/3):
    print('You need more practice')
    # If the amount correct is greater than 1/3 and less than 2/3 of the total
elif correct <= (amount/3):
    print('Please ask your math teacher for help!')
    # If the amount correct is less than 1/3 of the total amount prints
