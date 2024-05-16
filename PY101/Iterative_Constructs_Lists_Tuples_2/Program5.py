'''
Problem Statement:
String encoding s = "we love python very much”
i)	the first letter of each word is printed at the end.
ii)	In the second case, after each character, a p is printed.
'''

#(string0) string, given as input 
string0= "we love python very much"
print("\n\n The input string is:\t", string0)
print()

#Splitting the input string and getting a new list(string1)
string1= string0.split(' ')
print(string1)


#"answer i"

#printing statements
print("\n Answer (i):")
print("\n\n   Output/Result: Printing the first letter of each word at the end: \n \n \t \t", end=' ')


#Using a 'while' loop, 'length' function, slicing and concatenation, to print the first letter of each word at the end; and printing it, as output.
i=0
string1[i]=string1[0]

while i<5:
    string2=string1[i][0]
    
    string3=string1[i][1:len(string1)]

    string4=string3 +string2
    print(string4, end=' ')

    i+=1



#"answer ii"

#printing statements
print("\n\n\n\n Answer (ii):")
print("\n\n   Output/Result: Printing a 'p' after each letter : \n \n \t \t", end=' ')


#Using a 'for' loop, 'join' function to print a 'p' after each letter; and printing it, as output.

for l in string1:
    
    l='p'.join(l)
    print(l,end='')
    print('p',end=' ')
    
print('\n \n \n')

