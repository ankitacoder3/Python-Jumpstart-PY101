'''
Problem Statement:
Construct dictionary phone_book with :
Key: number of entries,   Values: name, phone number, email, address)
and perform the following operations:
{1: [("Rashma",8105731555,"rashma@gmail.com","bangalore"),2:("Saritha",9582161900,"saritha@gmail.com","Mangalore"),3:("Bharathi",9276895311,"bharathi@yahoo.com" ,"Koimbatore"),
4:("deepthi",8976885553,"deepthi@gmail.com","bangalore"),5:("kakoli",8816121598,"kakili@gmail.com","dispur")]}

   i) Add a new number to phone_book
  ii)  delete entry from phone book.

'''  
print('\nCalculate Phone_book.py\n')

print('Dictionary phone_book with operations. ')

#make a new  dictionary containing a few names and required details, for the phone book.
details=[("Rashma",8105731555,"rashma@gmail.com","bangalore"),("Saritha",9582161900,"saritha@gmail.com","Mangalore"),("Bharathi",9276895311,"bharathi@yahoo.com","Koimbatore"),  ("deepthi",8976885553,"deepthi@gmail.com","bangalore"),("kakoli",8816121598,"kakili@gmail.com","dispur")]
phone_book=dict(enumerate(details,1))
print("\nInput:")
print("\n'KEY' : 'VALUE' ")
for key,value in phone_book.items():
    print(key, ' : ',value)

#output
print("\nOutput:")

#adding  a new value to dictionary and printing the final dictionary
print("\n (i): adding  a new value to dictionary and printing the final dictionary ")
phone_book[len(phone_book)+1]=("Saanvi", 7878445362,"saanvi.33@gmail.com","Nagaland")
print("\n'KEY' : 'VALUE' ")
for key,value in phone_book.items():
    print(key, ' : ',value)

#deleting  a value from dictionary and printing the final dictionary
print("\n (ii): deleting  a value from dictionary and printing the final dictionary\n ")
del_k=int(input("Enter a key to be deleted: "))
del phone_book[del_k]
print("\n'KEY' : 'VALUE' ")
for key,value in phone_book.items():
    print(key, ' : ',value)

print()