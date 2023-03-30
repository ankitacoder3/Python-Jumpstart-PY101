'''
Problem Statement:
Enter marks of students till you need to stop. 
a) Find maximum marks
b) Find number of students who have scored highest
c) Find second highest marks
d) Enter fail marks and remove if fail marks present in list
'''

#getting input for no. of students, n
n =int(input("Enter number of students: "))

#entering the marks for n students
x=0
marks=[]
while(x<n):
        Y= int(input(f"Enter marks for student {x}:"))
        marks.append(Y)
        x=x+1

#sorting list
marks= sorted(marks)
print(sorted(marks))

#the maximum marks
mx = marks[n-1]
print("The maximum or highest mark scored by a student is: ",mx)

#no. of students that scored maximum marks
mx_count=0
for mark in marks:
        if mark==mx:
                mx_count+=1    
print("The number of students that scored maximum marks is/are:",mx_count)

#the second highest marks
mx2 = marks[n-2]
print("The second highest mark scored by a student is:",mx2)

#removing the marks which are below pass marks or have failed
#by defining a new empty list, final_list
final_list = []
fail_mark = 40
for mark in marks:
        if mark > fail_mark:
                final_list.append(mark)
        else:
                print("The marks that is below or equal to fail is/are:", mark)
        
#printing the final list
print("The final list is:",final_list)





