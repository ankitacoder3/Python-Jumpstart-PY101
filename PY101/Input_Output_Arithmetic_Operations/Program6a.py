'''
Problem Statement:
Swap the contents of two memory locations Using temporary variable.
'''
print('\nCalculate Swapping_with_temporary_variable.py\n')

#Getting input for the variables a and b.
print('Input values')
a= (input("a: "))
b= (input("b: "))

#swaping using a temporary variable.
c=a
a=b
b=c

#output
print("\nAfter swapping values a and b (using a tempory variable), a= {}, and b= {}.". format (a, b))
print()