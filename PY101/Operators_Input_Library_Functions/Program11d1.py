'''
Problem Statement:
Write a Python program to round the value of -4.3 and then takes the absolute value of that result.
'''
print('\nCalculate Round_absolute.py\n')

#v value
v = -4.3
print(f"Given value: {v} ." )

#calculate
import math
x = round(v)
x = math.fabs(x)

#printing the process
print("\nProcessing: ")
print("  To get absolute value,\n  use the 'fabs' function from the 'math' library.\n")
print("  To get rounded value,\n  use the 'round' function.")

#output
print(f"\n The result is {x}." )
print()