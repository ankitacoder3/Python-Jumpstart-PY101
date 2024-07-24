'''
Problem Statement:
Increment a given number by 5, for n number of times,
using Closure.
'''
print('\nCalculate Closure_increment_N_times.py\n')

#Defining the Count function. 

def Count(n):
    def incrementcount():
        return n+5
    return incrementcount


#Getting the input, a number.
print('Enter a number \'n\', to be incremented by 5, \'n\' no. of times.\n')
n=int(input('Enter the number, n: '))
print()
val=n

#Printing the output, by using 'for' loop and, by calling the function (by using 'closure concept').
for i in range(n):
    c=Count(val) #c refers to Count
    val=c() #to get value in c, need to call c [c()]
    print(f'After Increment No. -> {i+1}, value of number n: {val}')

print('\nFinal Result:\n After',n,'increments to the number',n,',\n \t \t the result is -> ',val)
print()