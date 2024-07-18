'''
Problem Statement:
Write a Python program to calculate multiplication of two random float numbers
'''
print('\nCalculate Multiplication_of_2_random_numbers.py\n')

#2 random float point numbers
import random
x= random.random()
y= random.random()

#calculation
result = ( x * y )

#output
print(f" 1- The two random float point numbers are:\n\t x = {round(x,4)}, and y = {round(y,4)} .\n" )
print(f" 2- The multiplication of the two random float point numbers is: \n\t {round(x,4)} * {round(y,4)} = {round(result,3)} . " )
print()