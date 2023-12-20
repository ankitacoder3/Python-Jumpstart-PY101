'''
Problem Statement:
Write a Python program to calculate distance between two points using latitude and longitude.
'''

#getting input for the latitudes and the longitude for the two points, and tlongitudepecasting the values.
latitude1= float(input("latitude1:"))
longitude1= float(input("longitude1:"))
latitude2= float(input("latitude2:"))
longitude2= float(input("longitude2:"))

#calculating the distance.
distance= (((latitude2 - latitude1)**2) + ((longitude2 -longitude1)**2)) ** 0.5


#output
print("The distance between the two points, using latitudes and longitudes, is {}". format (distance))




