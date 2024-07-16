'''
Problem Statement:
A.  display given list of data as mac address. { mac=['00','11','23','45','67','70'] }
B.  send festival greetings to friends, all friends in the list. { frnd=['ram',' sita',' raj',' joy',' joe'] }

C.  Given , Roll no’s as strings each separated by space, replace ROLL_NO_ in place of ROLL_ in first 3 roll no’s. Also find if user given roll no. is present or not.
roll_no = "ROLL_01 ROLL_02 ROLL_03 ROLL_04 ROLL_05 ROLL_06 ROLL_07 ROLL_08 ROLL_09 ROLL_10"
'''
print('\nCalculate List_join_replace.py\n')

#"answer A"

#list of values, given as input
print('PART A')
mac=['00','11','23','45','67','70']
print(f'Input is: {mac}')

#use the 'join' function to make the mac addresses, and print it as output.
print('\n Output (using join):')
print(':'.join(mac))
print()

#"answer B"

#list of names of friends, given as input
print('PART B')
friend=[' ram',' sita',' raj',' joy',' joe','']
print(f'Input is: {friend}')

#use the 'join' function to make the greetings, and print it as output.
print('\n Output (using join):')
print(', Happy Festival! \n'.join(friend))
print()

#"answer C"

#list of roll numbers of students, given as input
print()
print('PART C')
roll_no = "ROLL_01 ROLL_02 ROLL_03 ROLL_04 ROLL_05 ROLL_06 ROLL_07 ROLL_08 ROLL_09 ROLL_10"
print(f'Input is: {roll_no}')

#replacing 'ROLL_' with 'ROLL_NO_', for firt three roll no's, and printing it as output.
print('\n Output :')

full_roll_no=roll_no.replace('ROLL_','ROLL_NO_',3)
print ("1- After replacing 'ROLL_' with 'ROLL_NO_', for firt three roll no's :")
print (full_roll_no)


#checking if a particular roll_no is present or not

#taking input from user, for the roll_no that has to be searched for.
#using while loop to search for 3 roll_no's.
print()

n=0
print ("2- Searching for upto three roll no's :-\n")
while n<3:
    print('Enter \'-1\' to exit.')
    find=input("Enter ROLL NO. to be searched (in the format 'ROLL_xx'): ")

#splitting the roll_no string
    list=roll_no.split(' ')

#using the 'for' loop and if condition, to search for that particular roll number.
    f=roll_no.find(find.upper())
    f=2
    if (f>=0 and find!="-1"):
        print(f"{find} is PRESENT. ")
    elif(f<0 or find=='-1'):
        print('\nEnding search.\nThank you...')
        break
    else:
        print("ROLL NO. is NOT present or found.")
    print()
    n+=1
print()