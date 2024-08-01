'''
Problem Statement:
Write a program to Swap the contents of two memory locations using bitwise XOR operation. 
Note: Do not use either temporary variable or arithmetic operators.
'''
print('\nCalculate Swapping_using_xor.py\n')

#Getting input for the variables a and b.
a= int(input("Enter integer a: "))
b= int(input("Enter integer b: "))

#swaping using XOR.
a=a^b
b=a^b
a=a^b

#output
print("\n After swapping values a and b ( using XOR ),\n a = {}, and b = {} 43.". format (a, b))
print()