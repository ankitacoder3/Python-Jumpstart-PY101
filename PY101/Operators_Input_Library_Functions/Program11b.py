'''
Problem Statement:
Write a Python program to convert radian to degree.
'''
print('\nCalculate Radian_to_degree.py\n')

#getting input for angle.
rad= float(input("Enter Angle (in radians): "))

#conversion
import math
deg = math.degrees(rad)

#output
print(f"\n The angle is {round(deg,3)} degrees ." )
print()