'''
Problem Statement:
Write a Python program to generate a floating-point number within a range.
'''
print('\nCalculate Generate_random_float_number_in_range.py\n')

#get input for the range values
a= float(input("Enter a: "))
b= float(input("Enter b: "))

#random number in the range (a,b)
import random
result= random.uniform(a,b)

#output
print(f"\n The random float point number,\n\t in the range from {a} to {b},\n\t\t\t\t is {round(result,3)} ." )
print()