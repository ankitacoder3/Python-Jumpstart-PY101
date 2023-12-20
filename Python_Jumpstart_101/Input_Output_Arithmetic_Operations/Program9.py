'''
Problem Statement:
A school decided to replace the desks in three classrooms.
Each desk sits two students. Given the number of students in each class,print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

Sample: In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.


'''

#Getting input for the number of students in class 1, class 2 and class 3.

class1= int(input("Enter no. of students in classroom 1:"))
class2= int(input("Enter no. of students in classroom 2:"))
class3= int(input("Enter no. of students in classroom 3:"))

#Calculations
total_students = class1 + class2 + class3
if(total_students%2==1):
    total_students=total_students+1
benches = int(total_students / 2)


#output
print("The minimum number of benches to be purchased  is {}.". format (benches))
