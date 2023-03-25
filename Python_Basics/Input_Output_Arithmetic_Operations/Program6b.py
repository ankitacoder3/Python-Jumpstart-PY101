'''
Problem Statement:
Swap the contents of two memory locations Without using temporary variable.

'''

#Getting input for the variables a and b.

a= int(input("a:"))
b= int(input("b:"))


#swaping without using a temporary variable.
a=a+b
b=a-b
a=a-b

#output
print("After swapping values a and b (without using a tempory variable), a= {}, and b= {}.". format (a, b))
