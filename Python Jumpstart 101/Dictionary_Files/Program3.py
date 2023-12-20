'''
Problem Statement:
Given list of students, marks for phy,chem,maths and biology form a dictionary where key is SRN and values is dictionary containing PCMP marks of respective student.
srns = ["PECS001","PECS015","PECS065","PECS035","PECS038"]
p_marks = [98,99,85,92,79]
c_marks = [91,90,84,98,99]
m_marks = [78,39,60,50,84]
b_marks = [95,59,78,80,89]
'''  

#Giving 3 new input lists.

srns = ["PECS001","PECS015","PECS065","PECS035","PECS038"]
phy_marks = [98,99,85,92,79]
chem_marks = [91,90,84,98,99]
math_marks = [78,39,60,50,84]
bio_marks = [95,59,78,80,89]

#Make 2 new dictionaries.
student_marks={}
mark_det={}


#Use 'for' loop, to get the desired output dictionary.
for k in range(len(srns)):
   mark_det['phy']= phy_marks[k] 
   mark_det['chem']=chem_marks[k]
   mark_det['math']=math_marks[k]
   mark_det['bio']= bio_marks[k]
   
   #making desired dictionary
   student_marks[srns[k]]= mark_det


#Print the output dictionary.
print(student_marks)
