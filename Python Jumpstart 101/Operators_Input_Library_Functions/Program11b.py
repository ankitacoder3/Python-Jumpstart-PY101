'''
Problem Statement:
Write a Python program to convert radian to degree.
'''

#getting input for angle.
rad= float(input("Angle (in radians):"))

#conversion
import math
deg = math.degrees(rad)

#output
print(f"The angle is {deg} degrees." )
