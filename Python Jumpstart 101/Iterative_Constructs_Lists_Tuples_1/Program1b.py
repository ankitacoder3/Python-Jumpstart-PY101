'''
Problem Statement:
Find factorial of a number
'''


#getting input for natural  number(n).
n= int(input("Enter a natural number,n:"))

#fixing values of x to 1 and defining factorial
x=1
factorial=1

#using the while loop, for finding the factorial.
while(x<=n):
    factorial = factorial*x
    x = x+1

#output
print(factorial)
  
