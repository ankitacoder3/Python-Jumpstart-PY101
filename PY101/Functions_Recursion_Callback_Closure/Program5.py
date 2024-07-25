'''
Problem Statement:
Using Concept of Closure and Callback,
find nth fibonnaci number.
'''
print('\nCalculate Callback_Closure_Nth_Fibonnaci.py\n')

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
print('\nCalculating nth fibonacci no. ...\n ')

print('  Enter a number \'n\', to get the sum till \'n\'th fibonacci no. .\n')

number=int(input('  Enter the number, n: '))

#Results 
fib=store(number, fibonnaci) #needed as fib refers to store

#Printing the output,  by calling the function (by using 'closure concept').
print('\nFinal Result:\n\n\tSum till',number,'th fibonacci number is -> ')
print('\t\t\t\t\t     ',fib())

#calling fib, to print result
#print(fib) -> gives diff output
print()