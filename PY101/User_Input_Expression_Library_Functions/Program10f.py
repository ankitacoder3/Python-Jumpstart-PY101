'''
Problem Statement:
Write a Python program to generate the same random number every time.
'''
print('\nCalculate Generate_same_random_number_everytime.py\n')

#to generate the same random number everytime
import random
random.seed(7) 
x = random.random() 

#printing  the process
print("Processing: ")
print("  To generate the same random number everytime,\n  the 'seed' function from the 'random' library should be used.")

#output
print(f"\n The random integer number is -> {x} ." )
print()