'''
Problem Statement:
Swap the contents of two memory locations Without using temporary variable.
'''
print('\nCalculate Swapping_without_temporary_variable.py\n')

#Getting input for the variables a and b.
print('Input values')
a= float(input("a: "))
b= float(input("b: "))

#swaping without using a temporary variable.
a=a+b
b=a-b
a=a-b

#output
print("\nAfter swapping values a and b (without using a tempory variable), a= {}, and b= {}.". format (a, b))
print()
