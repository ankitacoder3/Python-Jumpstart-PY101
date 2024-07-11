'''
Problem Statement:
a) Read movie data from mov1.csv file. The CSV file mov1.csv has three columns- column1
    has year, column2 has rating, and column3 has movie name
b) Write year of release and movie name from mov1.csv to a text file
'''

print('Program to read movie data from mov1.csv file and write data to a text file.')

#create a empty dictionary
movie_det={}

#initializing the index for the dictionary
count=0

#part a

#Opening a file.
F=open('mov1.csv')

#Reading from that file, and using 'strip'.
Line=F.read()
Line=Line.strip()

#Create a list from each line of the csv, and append the details to the dictionary
for i in Line:
    
    #Use 'split', based on ','  to get the values of year, rating, etc.
    #l1=i.split(',')
    l1=i

    movie_det[count]=l1
    count+=1 #increment count

#Printing the READ details using the dictionary, as output for part(a).
print("\npart (a): ")

print("\n'Sl. No.' | ['Year', 'Ratings', 'Movie-name' ] \n \n ")
for key,value in movie_det.items():
    print(key, ' : ', value)
print()

#Closing the file.
F.close()


#part b

#Opening 2 files, one of them is text-editor(opened in write mode).
f1=open('mov.txt','w')
f2=open('mov1.csv','r')

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
