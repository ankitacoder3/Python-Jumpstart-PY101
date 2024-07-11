'''
Problem Statement:
N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
How many apples will each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for the questions above.	
'''
print('\nCalculate Apples_in_basket.py\n')

#getting input from user for N and K, and typecasting the values.
N= int(input("Enter no. of students, N: "))
K= int(input("Enter no. of apples, K: "))

#the no. of apples each student gets(//)
Each_student= K//N

#the no. of apples remaining in basket(%)
In_basket= K%N


#output
print("\nEach student will get {} apples, and {} apples will remain in the basket.". format (Each_student, In_basket))
print()