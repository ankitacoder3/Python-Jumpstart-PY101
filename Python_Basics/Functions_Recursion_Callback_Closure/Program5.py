'''
Problem Statement:
Using Concept of Closure and Callback,
find nth fibonnaci number.
'''

#Defining the fibonnaci function, and the store function. 
    
def fibonnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonnaci(n-1) + fibonnaci(n-2))

def store(n, a):
    def restore():
        return a(n)
    return restore
    #no 'restore()'  call, as we need to return a value. [Also, 'return restore', indirectly calls restore]

#Above parameter 'a' performs callback, and parameters 'a', 'n' perform closure.

#Getting the input.
number= int(input('\nEnter a number, to get the fibonacci sum til that no.:'))

fib=store(number, fibonnaci) #needed as fib refers to store

#Printing the output,  by calling the function (by using 'closure concept').
print(fib())

#calling fib, to print result
#print(fib) -> gives diff output

