'''
Problem Statement:
Write a program to Swap the contents of two memory locations using bitwise XOR operation. 
Note: Do not use either temporary variable or arithmetic operators.
'''

#Getting input for the variables a and b.

a= int(input("a:"))
b= int(input("b:"))


#swaping using XOR.
a=a^b
b=a^b
a=a^b

#output
print("After swapping values a and b ( using XOR), a= {}, and b= {}.". format (a, b))
