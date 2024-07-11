'''
Problem Statement:
Given the integer N - the number of seconds that is passed since midnight - how many full hours and full minutes are passed since midnight?
The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 1339).
For example, if N = 3900, then 3900 seconds have passed since midnight. Therefore, the time now is 1:05am.
So the program should print 1 65 - 1 full hour is passed since midnight, 65 full minutes passed since midnight.
'''
print('\nCalculate Since_midnight.py\n')

#Get input as, the number of seconds passed since midnight.
sec= int(input("Enter the number of seconds passed since midnight: "))

#Conversions, using truncated division.
hr = sec//3600
min = sec//60

#output statement
print("\nThe no. of full hours that passed since midnight is {}; \nAnd the no. of full minutes that passed since midnight is {}.". format (hr, min))

#output as numbers
print("\nOutputing the integers as: {hr} {min} .")
print(" {}  {}". format (hr, min))
print()