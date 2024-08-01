'''
Problem Statement:
Python Program to Find the Gravitational Force Acting Between Two Objects
'''
print('\nCalculate Gravitational_force.py\n')

#getting input for the `2 masses m1 and m2, and for distance between them. 
m1= float(input("Enter mass1 (in kg): "))
m2= float(input("Enter mass2 (in kg): "))
r= float(input("Enter Distance between the two masses (in m): "))

#defining G (gravitational constant).calculating the gravitational force.
G=(6.67)*(10**-11)
force= (G*(m1*m2)) /(r **2)

#output
print("\n The gravitational force between the two points is {:0.3e} Newton". format (force))
print()