'''
Libraries and Functions always come in handy to developers by allowing reusability of existing code. There are certain well known inherent
libraries that you have access to after installing python. By using these libraries and functions in them, write
a program (in Python 3) to guess a randomly generated number between 1 and 10.
For Example:
Guess the number: 4
Wrong, try again!
Guess the number: 8
Correct!
Hint: Figure out which library the “randint” function belongs to.
'''
import sys
import random
randomnum = (random.randint(0,10))
#print(randomnum)
while True:
    try:
        myinput = int(input(("Guess the number: ")))
        if myinput == randomnum:
            print("Correct!")
            break
        else:
            print("Wrong, try again. Please enter a number between 1 and 10")
    except (IndexError, ValueError) as e:
# Indicates invalid parameter was provided
        print("You must provide a number as a parameter to this script")
        print("Example: ")
        print("  1")
        sys.exit(1)




