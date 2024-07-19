'''
Problem Statement:
Reverse the given string using recursion.
'''
print('\nCalculate Reverse_string.py\n')

#Defining reverse string function.

def Reverse(string):
    if len(string)==0:
        return string
    else:
        return Reverse(string[1:]) + string[0]
   
            
#Getting input, for string.
strings= input('Enter text: ')

#Printing the output, by calling the function.
print('\nOutput : ')
print('\t',Reverse(strings),'\n')
print()