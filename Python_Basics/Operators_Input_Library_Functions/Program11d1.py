'''
Problem Statement:
Write a Python program to round the value of -4.3 and then takes the absolute value of that result.
'''

#v value
v= -4.3

#calculate
import math
x = round(v)
x = math.fabs(x)

#output
print(f"Given value: {v}." )
print(f"The result is {x}." )
