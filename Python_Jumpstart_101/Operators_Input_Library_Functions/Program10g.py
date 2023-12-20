'''
Problem Statement:
Write a Python program to roll a dice in such a way that every time you get the same number.
'''


#to generate the same number on the dice everytime
import random
random.seed(3) 
x= random.randrange(1,7) 


#output
print(f"The digit on the dice is {x}." )

