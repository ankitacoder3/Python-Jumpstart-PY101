'''
Problem Statement:
a)Read movie data from mov1.csv file. CSV file mov1.csv has three columns c1
   has year,c2 has rating,c3 has movie name.
b) write year of release and movie name from mov1.csv to a text file
'''

#part a

#Opening a file.
F=open('mov1.csv')

#Reading from that file, and using 'strip'.
Lin=F.read()
Lin=Lin.strip()

#Printing the lines, as output for part(a).
print("\n \t part (a): \n \n Year, Ratings, Movie-name \n \n",Lin)

#Closing the file.
F.close()


#part b

#Opening 2 files, one of them is text-editor(opened in write mode).
f1=open('mov.txt','w')
f2=open('mov1.csv')

#Reading the file, using 'readline'.
Li=f2.readline()

#Using 'while' loop , 'strip' and 'split'.
while Li:
   Li=Li.strip()
   R=Li.split(",")
   f1.write(R[0]+' '+R[2]+''+'\n')

#Closing the file.
f1.close()
f2.close()

#Verifying, by opening file.
f1=open('mov.txt')
lin=f1.read()
lin=lin.strip()
print("\n \ n \t part b: \n Year, Movie \n \ n",lin)
