'''
Problem Statement:
From file mov1.csv make a dictionary with Key as year and
values as name of movies released in that year.
'''

print('Program to read movie data from mov1.csv file and create a dictionary.')

#Opening the file.
F=open('mov1.csv')

#Reading from that file.
Line=F.readline()

#Creating a new dictionary.
dictionary={}

#Using 'while' loop , 'strip' and 'split'.
while Line:
   Line=Line.strip()
   L=Line.split(",")
   dictionary[L[0]]=L[2]
   Line=F.readline()
   
#Printing dictionary, as output.
print("\n'Year' : 'Movie-name'  \n")
for key,value in dictionary.items():
    print(key, ' : ', value)
print()

#Closing the file.
F.close()





