'''
Problem Statement:
Write a Python program to generate a floating-point number within a range.
'''


#get input for the range values
a= float(input("a:"))
b= float(input("b:"))

#random number in the range (a,b)
import random
result= random.uniform(a,b)

#output
print(f"The random float point number, in the range from {a} to {b}, is {result}." )


