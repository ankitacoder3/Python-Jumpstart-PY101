'''
Problem Statement:
Write a python program to perform the following operations using given list as input:
Given a heterogenous list, create separate lists for different types of data.
Write a python program to achieve the same.
'''


#defining the sample list
list= [10,4,6,8,'ábc','xyz','a','h',5.4,4.6,11.777,"today is an amazing day"]
print('The sample list is:', list)

#defining three new empty lists, for further analysis.
list_1=[]
list_2=[]
list_3=[]

#using "for" loop and if condition for classifying. 
for L in list:
    c=type(L)
    if (c== int):
        list_1.append(L)
    elif(c== str):
        list_2.append(L)
    elif(c== float):
        list_3.append(L)


#output
        
print(" ")
print ("The sample list can be divided into the following lists, based on its type- ")
print(" ")
        
print ("Type-'integer':",list_1)
print ("Type-'string':",list_2)
print ("Type-'float':",list_3)
        

