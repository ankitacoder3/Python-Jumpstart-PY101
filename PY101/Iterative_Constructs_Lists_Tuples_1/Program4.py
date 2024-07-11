'''
Problem Statement:
Enter marks of students till you need to stop. 
a) Find maximum marks
b) Find number of students who have scored highest
c) Find second highest marks
d) Enter fail marks and remove if fail marks present in list

'''
print('\nCalculate Marks_of_students.py\n')

#getting input for no. of students, n
n =int(input("Enter number of students: "))

#entering the marks for n students
print('\nInput marks-')
x=0
marks=[]
while(x<n):
        Y= int(input(f"Enter marks for student {x}: "))
        marks.append(Y)
        x=x+1

#sorting list
print("\nList of student marks:", marks)
marks= sorted(marks)
print("\nList of sorted student marks:", marks)

#Output
print("\nOutputs:-")
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

#defining a new empty list, final_list, to keep track of student marks that have pass marks
final_list = []
#define another list, to keep track of failed marks
fail=[]
fail_mark = 40

#removing the marks which are below pass marks or have failed
for mark in marks:
        if mark > fail_mark:
                final_list.append(mark)
        else:
                fail.append(mark)
print("The marks that is below or equal to fail is/are:", fail)
        
#printing the final list
print("\nThe final list of student marks is:",final_list)
print()