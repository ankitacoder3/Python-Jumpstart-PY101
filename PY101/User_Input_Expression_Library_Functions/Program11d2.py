'''
Problem Statement:
Write a Python program that takes the ceiling of sine of 34.5.
'''
print('\nCalculate Ceil.py\n')

#v value
v= 34.5
print(f"Given value: {v} ." )

#calculate
import math
x = math.sin(v)
x = math.ceil(x)

#printing the process
print("\nProcessing: ")
print("  To get ceil value,\n  use the 'ceil' function from the 'math' library.\n")
print("  To get sine value,\n  use the 'sine' function from the 'math' library.")

#output
print(f"\n The result is {x}." )
print()