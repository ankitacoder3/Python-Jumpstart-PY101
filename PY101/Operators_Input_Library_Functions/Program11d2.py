'''
Problem Statement:
Write a Python program that takes the ceiling of sine of 34.5.
'''

#v value
v= 34.5

#calculate
import math
x = math.sin(v)
x = math.ceil(x)

#output
print(f"Given value: {v}." )
print(f"The result is {x}." )
