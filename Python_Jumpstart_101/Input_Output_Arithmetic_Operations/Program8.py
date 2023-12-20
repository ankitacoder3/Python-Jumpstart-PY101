'''
Problem Statement:
Given the distance between 2 cities in kilometers. Write a Python program convert it into meters, centimeters, feet and inches and display the result.
'''

#Getting input for the distance between 2 cities in kilometers .

km= float(input("Enter the distance between 2 cities in kilometers:"))


#Conversions.
m = km * 1000
cm = m * 100
ft = cm * (1/30.48) 
inc = cm * (1/2.54) 


#output
print("The distance between the two cities is {} meters.". format (m))
print("The distance between the two cities is {} centimeters.". format (cm))
print("The distance between the two cities is {} feet.". format (ft))
print("The distance between the two cities is {} inches.". format (inc))
