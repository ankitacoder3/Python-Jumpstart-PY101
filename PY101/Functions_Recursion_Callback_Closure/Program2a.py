'''
Problem Statement:
Reverse the given string using recursion.
'''

#Defining reverse string function.

def Reverse(string):
    if len(string)==0:
        return string
    else:
        return Reverse(string[1:]) + string[0]
            

#Getting input, for string.
strings= input('\nEnter text:')

#Printing the output, by calling the function.
print('\nOutput : ')
print(Reverse(strings),'\n')
