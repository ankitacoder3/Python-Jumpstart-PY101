'''
Problem Statement:
Increment a given number by 5, for n number of times,
using Closure.
'''
print('\nCalculate Callbacks.py\n')

#Defining the Count function. 

def Count(n):
    def incrementcount():
        return n+5
    return incrementcount


#Getting the input, a number.
print('Enter a number \'n\', to be incremented by 5, \'n\' no. of times.\n')
n=int(input('Enter the number, n:'))
val=n

#Printing the output, by using 'for' loop and, by calling the function (by using 'closure concept').
for i in range(n):
    c=Count(val) #c refers to Count
    val=c() #to get value in c, need to call c [c()]
    print(f'Increment-{i}, value: {val}')

print('\nFinal Result:',val)
print()