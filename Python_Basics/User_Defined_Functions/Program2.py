'''
Problem Statement:
Find minimum element, in a homogeneous list given by user, 
by calling a user defined function.

#Incase of strings, take minimum as smallest lexicographic value
'''

#Defining the homogenous function.

def homogeneous(L):

    #Getting input from user for the type of data, and number of elements.
    N=int(input('\nEnter number of elements, for making list, n:'))
    print("\nData-types: int, float, str.")
    t=input("Enter type of data:")
    print()

    #Using the if-else condition, to check the datatype.
    #Using while loop, to get input from users for N values, and appending these N values to the list L.
    
    
    if (t=="int" or t=="str" or t=="float"):
        i=0
        try:
            while (i<N):
                Li=input("enter list element: ")
                if (t=="int"):
                    L.append(int(Li))
                elif (t=="float"):
                    L.append(float(Li))
                elif (t=="str"):
                    L.append(str(Li))
                i+=1
        except:
            print('Invalid input! Try Again!\n')
            return
        
        #Printing the list
        print('\n The given list is:')
        print(L)
    
        #Defining the minm (minimum) function. 
        def minm(a):
            i=0

            #Using closure concept, for N and L.

            #Defining new variable, mn(min value).
            mn= L[0]

            #Using while loop and if condition, to get mn.
            while (i<N):
                if L[i]<mn:
                    mn= L[i]
                i+=1

            #Printing the mn, as output.
            print('\n The minimum element in user-given list(L) is: ',mn)

        #Calling the minm function
        minm(L)
                    
    else:
        print('\nInvalid data type! Try again!\n')

#Defining new empty list
L=[]

#Calling the homogeneous function
homogeneous(L)

print()