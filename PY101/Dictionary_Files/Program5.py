'''
Problem Statement:
From file mov1.csv make a dictionary with Key as year and
values as name of movies released in that year.
'''
print('\nCalculate Creating_dictionary_from_csv.py\n')

print('Read movie data from mov1.csv file and create a dictionary.')

#Opening the file.
F=open('mov1.csv')

#Reading from that file.
Line=F.readline()

#Creating a new dictionary.
dictionary={}

#Using 'while' loop , 'strip' and 'split'.
count=0
while Line:
   Line=Line.strip()
   L=Line.split(",")
   dictionary[L[0]]=L[2]
   Line=F.readline()
   count+=1
print('\nRead ',count," records, from the CSV file.")
   
#Printing dictionary, as output.
print("\n'Year' : 'Movie-name'  \n")
for key,value in dictionary.items():
    print(key, ' : ', value)

print('\nRead ',len(dictionary)," records.")
print('Records outputed are lesser than the records inputed.\nThis is because the \'key\' in dictionary is unique. As, one key stores one value.\n')

#Part2- Preventing Data loss
print('\nPART2- Data loss prevention, using dictionary method.')

#Reopen and read the file again
F2=open('mov1.csv')
Line=F2.readline()

#Creating a new dictionary.
dictionary2={}

#Using 'while' loop , 'strip' and 'split'.
count=0
v=0
while Line:
   Line=Line.strip()
   L=Line.split(",")
   if(L[0] in dictionary2.keys()):
      dictionary2[L[0]].append(L[2])
      v+=1
   else:
      dictionary2[L[0]]=[L[2]]
      v+=1
   Line=F2.readline()
   count+=1

#Printing dictionary2, as output.
print("\n'Year' : 'Movie-name'  \n")
for key,value in dictionary2.items():
    print(key, ' : ', value)

print('\nRead ',len(dictionary2)," records.Read ",v," values.")

#Closing the file.
F.close()
F2.close()

print()