'''
Problem Statement:
From file mov1.csv make a dictionary with Key as year and
values as name of movies released in that year.
'''

#Opening the file.
F=open('mov1.csv')

#Reading from that file.
Lin=F.readline()

#Creating a new dictionary.
dictionary={}

#Using 'while' loop , 'strip' and 'split'.
while Lin:
   Lin=Lin.strip()
   Li=Lin.split(",")
   dictionary[Li[0]]=Li[2]
   Lin=F.readline()
   
#Printing dictionary, as output.
print(dictionary)

#Closing the file.
F.close()





