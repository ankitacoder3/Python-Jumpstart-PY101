'''
Problem Statement:
Write a program to read 4 characters separately from the user. Convert every character to its next alphabet.
'''

#Getting input for 4 alphabets.
a1= input("Enter alphabet 1:")
a2= input("Enter alphabet 2:")
a3= input("Enter alphabet 3:")
a4= input("Enter alphabet 4:")


#Converting and output
print( "The next alphabet of a1 is",chr(ord(a1)+1))
print( "The next alphabet of a2 is",chr(ord(a2)+1))
print( "The next alphabet of a3 is",chr(ord(a3)+1))
print( "The next alphabet of a4 is",chr(ord(a4)+1)) 
