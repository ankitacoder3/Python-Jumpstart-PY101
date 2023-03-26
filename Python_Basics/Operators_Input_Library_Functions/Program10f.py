'''
Problem Statement:
Write a Python program to generate the same random number every time.
'''

#to generate the same random number everytime
import random
random.seed(7) 
x= random.random() 


#output
print(f"The random integer number is {x}." )

