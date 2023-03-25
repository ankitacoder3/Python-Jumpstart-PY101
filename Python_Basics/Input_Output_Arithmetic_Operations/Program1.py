'''
Problem Statement:
Create a program that has two parameters namely name and their age. Print out a message addressed 
to them that tells them the year that they will turn 100 years old.
'''

#getting input from user for name and age, and typecasting the age from string to integer.
name= input("Enter name:")
age= int(input("Enter age:"))

#calculation
year = 2020+100 - age

#output
print("In the year {}, {} will turn 100 years old.". format (year, name))
