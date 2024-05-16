'''
Problem Statement:
Find length of given list.
'''

#Defining the leng(length) function.    
def leng(a):

    #Defining new variable, count.
    count=0

    #Using for loop, and iterating through the list, to get count.
    for i in a:
        count+=1

    #Printing the count, as output.
    print('\nThe length of the given list(L) is: ',count)

#Giving input list, L and printing it.
L=[88,99.999,6,7,22,44,88,993,22,86,188,2775,9990,7678,83456]
print('\n The given input list is: \n',L)

#Calling the leng function
leng(L)

print()