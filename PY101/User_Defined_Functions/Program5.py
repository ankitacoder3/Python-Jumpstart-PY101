'''
Problem Statement:
Given a list of integers, sort it in ascending order
(without using inbuilt sort).
'''

#Giving input for a L_int of integers(L_int), and printing it.
L_int=[77,999,7875,99,44,5,-4,-9,-4,-8,9,88,20,55,345,889,19,278,377,35,1,2,6,886,5778,5654,-200,-3243,-77,-7,9956,0,10]
print('\nThe input list is: \n',L_int)

#Defining ascending_sort function.
def ascending_sort(a):
    
    #Using closure concept, for L_int.
    
    #Defining variable, l (length of L_int).
    l=len(a)
    
    #Using for loop, while loop, and if condition , to get the result.
    j=0
    for j in range(l):
        i=0
        while (i<l-1):
            if L_int[i] > L_int[i+1]:
                L_int[i],L_int[i+1]=L_int[i+1],L_int[i]
            i+=1

    #Printing the result (list in ascending order), as output.
    print('\n The list sorted in ascending order is: \n',L_int)

#Calling the ascending_sort function
ascending_sort(L_int)

print()
