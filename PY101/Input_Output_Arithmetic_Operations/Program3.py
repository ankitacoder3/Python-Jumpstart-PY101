'''
Problem Statement:
Write a program to calculate the distance between two points.	
'''
print('\nCalculate Distance.py\n')

#getting input for the x and y coordinates for the points, and typecasting the values.
print('Input values')
x1= float(input("x1: "))
y1= float(input("y1: "))
x2= float(input("x2: "))
y2= float(input("y2: "))

#calculating the distance.
distance= (((x2 - x1)**2) + ((y2 -y1)**2)) ** 0.5


#output
print("\nThe distance between the two points is {}". format (distance))
print()