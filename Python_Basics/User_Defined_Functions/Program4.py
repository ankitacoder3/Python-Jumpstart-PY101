'''
Problem Statement:
Given a list of  strings, find the largest string,
and display the largest string alongwith its length.
'''

#Defining all functions

def length(x):
    count=0
    for j in x:
        count+=1
    return count

def long(l):
    max = l[0]
    for i in l:
        if length(max)<length(i):
            max=i
    return max


#Main Function

# INSTRUCTIONS:  make sure either 'OPTION A LINE' or 'OPTION B LINE' is not commented, as per preference

# OPTION A: Using 'user-input' value for 'String'
#Getting input from user, for a string.
String=input('\nEnter text : ')   # OPTION A LINE

# OPTION B: Using 'hard-coded' value for 'String'
#String='Today its is going to rain heavily' # OPTION B LINE

#Print given string
print('\nSTRING given is: ',String)

#Converting the string to a list, by splitting it.
L= String.split(' ')
l=[]
for i in L:
    l.append(i)

print('\nLIST after splitting the string: ',l)

largest_str=long(l)
largest_size=length(largest_str)

print(f'\nResult: The largest string is \"{ largest_str}\" of length \"{largest_size}\" letters. \n')
