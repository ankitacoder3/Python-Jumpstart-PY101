'''
Problem Statement:
Write a Python program to calculate distance between two points using latitude and longitude.
'''
print('\nCalculate Distance_longitude_latitude.py\n')

#getting input for the latitudes and the longitude for the two points, and tlongitudepecasting the values.
latitude1= float(input("Enter latitude-1 : "))
longitude1= float(input("Enter longitude-1 : "))
latitude2= float(input("Enter latitude-2 : "))
longitude2= float(input("Enter longitude-2 : "))

#calculating the distance.
distance = (((latitude2 - latitude1)**2) + ((longitude2 -longitude1)**2)) ** 0.5

#output
print("\n The distance between the two points,\n using the latitudes and longitudes values, is {:.3}". format (distance))
print()