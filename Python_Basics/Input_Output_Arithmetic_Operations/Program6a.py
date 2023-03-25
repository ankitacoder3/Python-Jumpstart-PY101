'''
Problem Statement:
Swap the contents of two memory locations Using temporary variable.

'''

#Getting input for the variables a and b.

a= int(input("a:"))
b= int(input("b:"))


#swaping using a temporary variable.
c=a
a=b
b=c



#output
print("After swapping values a and b (using a tempory variable), a= {}, and b= {}.". format (a, b))
