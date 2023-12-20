'''
Problem Statement:
Swap the contents of two memory locations Using temporary variable.

'''

#Getting input for the variables a and b.

a= (input("a:"))
b= (input("b:"))


#swaping using a temporary variable.
c=a
a=b
b=c



#output
print("After swapping values a and b (using a tempory variable), a= {}, and b= {}.". format (a, b))
