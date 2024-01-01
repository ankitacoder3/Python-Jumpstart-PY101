'''
Problem Statement:
Suppose a person wants to calculate the simple interest for the account he has taken for specified number of years.(read the values from user)
'''

#getting input for principle, time, rate of interest and typecasting the values.
principle= float(input("Enter principle (amount, in rupees):"))
time= float(input("Enter time(in years):"))
rate= float(input("Enter rate of interest:"))

#calculation
simple_interest = ((principle*rate*time)/100)

#output
print(f"The simple interest is {simple_interest} rupees." )
