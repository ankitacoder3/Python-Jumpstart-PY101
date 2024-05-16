'''
Problem Statement:
Use recursion to raise a number to a given power n.
'''

#Defining raised (n raised to p) function. 

def raised(n,p):
    if p==1:
        return n
    else:
        return n*raised(n, p-1)
            

#Getting the 2 inputs, number and power.
number= int(input('Enter the number(n), that has to be raised :'))
power= int(input('Enter the power(p), that the number has to be raised to :'))

#Printing the output.
print(raised(number,power))

