'''
Problem Statement:
Find maximum element, in a homogeneous list given by user, 
by calling a user defined function

#Incase of strings, take maximum as greatest lexicographic value
'''
print('\nCalculate Homogeneous_list_Max_element.py\n')

#Defining the homogenous function.
def homogeneous(L):

    #Getting input from user for the type of data, and number of elements.
    N=int(input('\nEnter number of elements, for making list, n: '))
    print("\nData-types: int, float, str.")
    t=input("Enter type of data : ")
    print()

    #Using the if-else condition, to check the datatype.
    #Using while loop, to get input from users for N values, and appending these N values to the list L.
    if (t=="int" or t=="str" or t=="float"):
        i=0
        try:
            while (i<N):
                Li=input("\tenter list element: ")
                if (t=="int"):
                    L.append(int(Li))
                elif (t=="float"):
                    L.append(float(Li))
                elif (t=="str"):
                    L.append(str(Li))
                i+=1
        except NameError:
            print('Invalid input! Try Again!\n')
            return
        
        #Printing the list
        print('\nThe given list is: \n\t',L)

        #Defining the maxm (maximum) function.    
        def maxm():
            i=0

            ''' Using closure concept, for N and L. '''

            #Defining new variable, mx(max value).
            mx= L[0]

            #Using while loop and if condition, to get mx.
            while (i<N):
                if L[i]>mx:
                    mx= L[i]
                i+=1

            #Printing the mx, as output.
            print('\n The MAXIMUM element in user-given list(L) is: ',mx, '\n')

        #Calling the maxm function
        maxm()
            
    else:
        print('\nInvalid data type! Try again!\n')

#Defining new empty list
L=[]

#Calling the homogeneous function
homogeneous(L)

print()