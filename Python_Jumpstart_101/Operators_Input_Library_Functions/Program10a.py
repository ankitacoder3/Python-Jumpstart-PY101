'''
Problem Statement:
Write a Python program to get a single random character from a specified string.
'''



#getting input for a string.
str= input("Enter text:")

#process
import random
chosen = random.choice(str)

#output
print("The random character got from the given string is {}.". format (chosen))


