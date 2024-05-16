'''
Problem Statement:
Find Nth root of a given Number,
by Closure.
'''

#Defining the Count function. 

#outer function
def n_root(a,n):

    #inner function
    def Root():

        #Printing input values
        print('a: ',a,' n: ',n)

        #Printing the output,
        print('Result- Nth root of \'a\' = a**(1/n) = ',a**(1/n))

    #call inner function
    Root()
    

#Getting the 2 inputs, a number (whose nth root has to be found).
number= int(input('\nEnter a number \'a\', whose nth root has to be found:'))
n=int(input('Enter n:'))

#Call the function, using 'closure concept'.
n_root(number,n)
