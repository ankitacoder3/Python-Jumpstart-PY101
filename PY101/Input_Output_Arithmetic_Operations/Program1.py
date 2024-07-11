'''
Problem Statement:
Create a program that has three parameters namely name, age, current year. Print out a message addressed 
to them that tells them the year that they will turn 100 years old.
'''
print('\nCalculate 100years_age.py\n')

#getting input from user for name and age, and typecasting the age from string to integer.
name= input("Enter name:")
age= int(input("Enter age:"))
current_year= int(input("Enter current year:"))


#calculation
year = current_year+100 - age

#output
print("\nIn the year {}, {} will turn 100 years old.". format (year, name))
print()