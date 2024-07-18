'''
Problem Statement:
Python Program to Clear the Rightmost Set Bit of a Number.
'''
print('\nCalculate Clear_RightMostBit.py\n')

#getting input for  NUMBER.
n= int(input("Enter a number: "))

#condition and output
print()
if((n & 1)== 1): 
    print(" RSB is set.")
    print(" After clearing RSB, the number is ",n &(n-1),".")
else:
    print(" RSB is already clear.")
print()