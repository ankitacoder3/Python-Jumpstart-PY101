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


#make a new  dictionary containing a few names and required details, for the phone book.
details=[("Rashma",8105731555,"rashma@gmail.com","bangalore"),("Saritha",9582161900,"saritha@gmail.com","Mangalore"),("Bharathi",9276895311,"bharathi@yahoo.com","Koimbatore"),  ("deepthi",8976885553,"deepthi@gmail.com","bangalore"),("kakoli",8816121598,"kakili@gmail.com","dispur")]
phone_book=dict(enumerate(details,1))
print("\n \t Input: \n ")
print(phone_book)

#adding  a new value to dictionary and printing the final dictionary
phone_book[len(phone_book)+1]=("Saanvi", 7878445362,"saanvi.33@gmail.com","Nagaland")
print("\n \n \t (i): \n ")
print(phone_book)

#deleting  a value from dictionary and printing the final dictionary
print("\n \n \t (ii): \n ")
del_k=int(input("Enter a key to be deleted:"))
del phone_book[del_k]
print("\n",phone_book)
