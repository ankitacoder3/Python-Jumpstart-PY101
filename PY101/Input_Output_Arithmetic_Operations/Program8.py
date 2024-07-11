'''
Problem Statement:
Given the distance between 2 cities in kilometers. 
Write a Python program convert it into meters, centimeters, 
feet and inches and display the result.
'''
print('\nCalculate KM_to_m_cm_feet_inches.py\n')

#Getting input for the distance between 2 cities in kilometers .
km= float(input("Enter the distance between 2 cities in kilometers(km): "))

#Conversions.
m = km * 1000
cm = m * 100
ft = cm * (1/30.48) 
inc = cm * (1/2.54) 

#output
print("\nThe distance between the two cities in meters is-> {:.3f} m.". format (m))
print("The distance between the two cities in centimeters is-> {:.3f} cm.". format (cm))
print("The distance between the two cities in feet is-> {:.3f} ft.". format (ft))
print("The distance between the two cities in inches is-> {:.3f} inc.". format (inc))
print()