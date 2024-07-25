'''
Problem Statement:
Find Nth root of a given Number,
by Closure.
'''
print('\nCalculate Closure_Nth_root.py\n')

#Defining the Count function. 

#outer function
def n_root(a,n):

    #inner function
    def Root():

        print('\nFinal Result:\n\n\tPROCESSING')

        #Printing input values
        print('\t\t  a: ',a,'\n\t\t  n: ',n)

        print('\n\tCALCULATING','\n\t\t  a ** ( 1 / n ) ', '\n\t\t  =',a,'** ( 1 /',n,') ')

        #Printing the output
        print('\t\t  =',a**(1/n) )

    #call inner function
    Root()
    

#Getting the 2 inputs, a number (whose nth root has to be found).
print('\nCalculating a^(1/n) expression ... \n  ')

print('  Enter a number \'a\', whose nth root has to be found.\n')
number=int(input('  Enter the number, a: '))
n=int(input('  Enter the number, n: '))
print()

#Call the function, using 'closure concept'.
n_root(number,n)
print()