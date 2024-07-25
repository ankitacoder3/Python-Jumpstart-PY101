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
print('\nCalculating n+(5*n) expression ...\n ')

print('  Enter a number \'n\', to be incremented by 5, \'n\' no. of times.\n')
n=int(input('  Enter the number, n: '))
print()
val=n

#Printing the output, by using 'for' loop and, by calling the function (by using 'closure concept').
for i in range(n):
    c=Count(val) #c refers to Count
    val=c() #to get value in c, need to call c [c()]
    print(f'\tAfter Increment No. -> {i+1}, value of number n: {val}')

print('\nFinal Result:\n\n\tAfter',n,'increments,\n \t  with the number 5 ,\n \t  to the number',n,',\n \t  the result is ->')
print('\n\t\t\t n + ( 5 * n ) \n\t\t\t =',n,'+ ( 5 *',n,') \n\t\t\t =',val)
print()