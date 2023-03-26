'''
Problem Statement:
Given a 4-digit integer number, display the individual digits & also compute the sum of digits. NOTE: without using loop’s and conversions.
'''

#Getting input for a 4-digit integer number.
integer = int(input("Enter a 4-digit integer number:"))

#Calculations
digit_1 = integer // 1000
integer = integer % 1000
digit_2 = integer // 100
integer = integer % 100
digit_3 = integer // 10
digit_4 = integer % 10
sum = digit_1 + digit_2 + digit_3 + digit_4

#output
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
print("sum: ",sum)
