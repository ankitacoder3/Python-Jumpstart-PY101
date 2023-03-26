'''
Problem Statement:
Python Program to Find the Gravitational Force Acting Between Two Objects
'''

#getting input for the `2 masses m1 and m2, and for distance between them. 
m1= float(input("mass1(in kg):"))
m2= float(input("mass2(in kg):"))
r= float(input("Distance between the two masses(in m):"))

#defining G (gravitational constant).calculating the gravitational force.
G=(6.67)*(10**-11)
force= (G*(m1*m2)) /(r **2)


#output
print("The gravitational force between the two points is {} Newton". format (force))


