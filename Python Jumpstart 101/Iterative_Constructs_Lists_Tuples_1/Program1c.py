'''
Problem Statement:
Prints all prime numbers from 2 - n
'''

#getting input for natural  number(n).
n= int(input("Enter a natural number,n:"))

#fixing values ‘term’ and printing 2.
term=2
print("2 ",end='')

#using the while loop, for getting the series.
while term<n:
    is_prime= True
    term+=1
    #all numbers are assumed prime until proven otherwise
    

#using the 'for' loop and if condition, for getting the term.
    for i in range(2,term):
        if(term%i==0):
            is_prime= False
            break
        else:
            i= i+1
        
    if is_prime:
            print(term, end=" ")    
print()

