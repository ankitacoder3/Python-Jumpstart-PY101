'''
Problem Statement:
Write a program to generate fibonacci series till n terms.
Including number 'n'.
'''
print('\nCalculate Fibonacci_numbers.py\n')

#getting input for number n.
n= int(input("Enter a number, n: "))

#fixing values of x and y, to 0 and 1 respectively
x=0
y=1

#printing output
print("\nFibonacci numbers till iteration ",n, " are as follows: ")

if (n==0):
    print("Enter a valid natural number! ")
elif (n==1):
    print(x,end=' ')
else:
    print(x,y,end=' ')

    #iterating x and y
    for I in range(2,n+1):
        new_no = x + y
        print(new_no,end=' ')
        x=y
        y=new_no

print()
print()