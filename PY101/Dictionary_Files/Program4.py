'''
Problem Statement:
a) Read movie data from mov1.csv file. The CSV file mov1.csv has three columns- column1
    has year, column2 has rating, and column3 has movie name
b) Write year of release and movie name from mov1.csv to a text file
'''
print('\nCalculate Read_csv_write_txt.py\n')

print('Read movie data from mov1.csv file and write data to a text file.')

#create 2 empty dictionary
movie_det={}
det={}

#initializing the index for the dictionary
count=0

#part a
print("\npart A: ")

#Opening the CSV in 'read' mode
F=open('mov1.csv','r')

#Reading from that file, and using 'strip'.
Line=F.read()
Line=Line.strip()

#Create a list from each line of the csv, by using 'split' on '\n'
l1=Line.split('\n')

#Append the details to the dictionary
for i in l1:
    
    #create another list, by using 'split' on ','
    l2=i.split(',')

    #appending to dictionary 'det'
    det['Year'] = l2[0]
    det['Rating'] = l2[1]
    det['Movie Name'] = l2[2]

    #appending to dictionary 'movie_det'
    movie_det[count]=det

    #reseting the values
    det={}

    count+=1 #increment count

#Printing the READ details using the dictionary, as output for part(a).
print("\n'Sl. No.' | ['Year', 'Ratings', 'Movie-name' ] \n ")
for key,value in movie_det.items():
    print(key, ' : ', value)
print('\nRead ',len(movie_det)," records.\n")


#part b
print("\npart B: ")

#Opening the  text-editor (in write mode).
f1=open('mov.txt','w')

#Using 'for' loop
# 1- to read the values from the dictionaries 'movie_det' and 'det'
# 2- to write the necessary values to the file f1
for key,value in movie_det.items():
    det=value
    for k,v in det.items():
      if(k=='Year'):
         f1.write(v+' ')
      elif(k=='Movie Name'):
         f1.write(v+'\n')

#Closing the files.
f1.close()
F.close()

#Verifying, by opening file.
f1=open('mov.txt')
line=f1.read()
line=line.strip()
line=line.split('\n')
print("\nYear, Movie \n")
for i in line:
   print(i)
print('\nRead ',len(line)," records.")
print()
