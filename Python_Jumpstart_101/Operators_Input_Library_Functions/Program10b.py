'''
Problem Statement:
Write a Python program to: 
i) shuffle students in a class. (Assume no of students in a class are 10)
ii) to choose one student who would become a Class representative.
iii) to create a random sample of size 2 from the available number of population who are the potential candidates to become event coordinators.

'''


#stating list of students.
import random
stu_list = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

#answer-1
#shuffling
random.shuffle(stu_list)
print("The given class is {}.". format (stu_list))

#anwer-2
#chosing for class representative
chosen = random.choice(stu_list)
print("The class representative is student no. {}.". format (chosen))

#anwer-3
#creating a random sample who can become event coordinators
chosen_1 = random.choice(stu_list)
chosen_2 = random.choice(stu_list)
print("The event coordinators are student no. {}, and student no. {}.". format (chosen_1, chosen_2))

