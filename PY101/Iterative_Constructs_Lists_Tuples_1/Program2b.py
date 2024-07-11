'''
Problem Statement:
Write a python program to perform the following operations using given list as input:
Sort in ascending order
 i)list of strings
 ii) list of number
'''
print('\nCalculate Sort_lists.py\n')

#string list values and number list values
string=['zap','yap','map']
number=[1,99,80,7]

#printing the unsorted lists
print("The unsorted lists are:", string, number)

#printing outputs- string_list, number_list
print("\nThe sorted lists are as follows:")

print("i. list of string in ascending order",sorted(string))
print("ii. list of number in ascending order", sorted(number))
print()