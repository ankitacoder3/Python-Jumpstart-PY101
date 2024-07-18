'''
Problem Statement:
Write a Python program to roll a dice in such a way that every time you get the same number.
'''
print('\nCalculate Generate_same_random_number_everytime_on_dice.py\n')

#to generate the same number on the dice everytime
import random
random.seed(3) 
x= random.randrange(1,7) 

#printing  the process
print("Processing: ")
print("  To generate the same random number everytime,\n  the 'seed' function from the 'random' library should be used.\n")
print("  To generate within the same range everytime,\n  the 'randrange' function from the 'random' library should be used.")

#output
print(f"\n The digit on the dice is -> {x} ." )
print()