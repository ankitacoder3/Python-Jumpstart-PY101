'''
Problem Statement:
Given a list of  strings, find the largest string,
and display the largest string alongwith its length.
'''
print('\nCalculate Find_largest_string.py\n')

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

# INSTRUCTIONS
print("   INSTRUCTIONS: \n\t Enter 'A' to use 'user-input' value for 'String' \n\t Enter 'B' to use 'hardcoded' value for 'String' \n")

# Inputting the choice
choice = input("   Enter Choice: ")

# flag:- to check if the 'Choice' input is correct
flag = 0

if( choice == 'A' ):
    # OPTION A: Using 'user-input' value for 'String'

    # Getting input from user, for a string.
    String = input('\n   Enter text: ')   

    # changing flag value, as correct 'Choice' input is given
    flag = 1 

elif( choice == 'B' ):
    # OPTION B: Using 'hard-coded' value for 'String'

    String='Today its is going to rain heavily' 

    # changing flag value, as correct 'Choice' input is given
    flag = 1 

else:
    print("\n  Invalid Choice! Try again...\n")

if ( flag == 1 ) :

    #Print given string
    print('\n INPUT: \n\t STRING given is: ',String)

    #Converting the string to a list, by splitting it.
    L= String.split(' ')
    l=[]
    for i in L:
        l.append(i)

    print('\n PROCESSING: \n\t LIST after splitting the string: ',l)

    largest_str=long(l)
    largest_size=length(largest_str)

    print(f'\n RESULT: \n\tThe LARGEST string is \"{ largest_str}\" of length \"{largest_size}\" characters. \n')
print()