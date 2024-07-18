'''
Problem Statement:
Write a Python program to generate a random integer number from the given range.
'''
print('\nCalculate Generate_random_int_number_in_range.py\n')

#a random integer number
import random
x = random.randint(20,60)

#output
print(f"\n The random integer number,\n\t in the range 20 to 60,\n\t\t\t      is {round(x,3)} ." )
print()