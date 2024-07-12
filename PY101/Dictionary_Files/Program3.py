'''
Problem Statement:
Given list of students, marks for physics, chemistry, maths, and biology form a dictionary where key is SRN and values is dictionary containing PCMB marks of respective student.
srns = ["PECS001","PECS015","PECS065","PECS035","PECS038"]
p_marks = [98,99,85,92,79]
c_marks = [91,90,84,98,99]
m_marks = [78,39,60,50,84]
b_marks = [95,59,78,80,89]
'''  
print('\nCalculate PCMB_marks.py\n')

print('Dictionary where the keys are SRN, and the values are the respective marks. ')

#Giving 3 new input lists.

srns = ["PECS001","PECS015","PECS065","PECS035","PECS038"]
phy_marks = [98,99,85,92,79]
chem_marks = [91,90,84,98,99]
math_marks = [78,39,60,50,84]
bio_marks = [95,59,78,80,89]

#Make 2 new dictionaries.
student_marks={}

#Use 'for' loop, to get the desired output dictionary.
for k in range(0,len(srns)):
   mark_det={}

   mark_det['Physics']= phy_marks[k] 
   mark_det['Chemistry']=chem_marks[k]
   mark_det['Mathematics']=math_marks[k]
   mark_det['Biology']= bio_marks[k]
   
   #making desired dictionary
   student_marks[srns[k]]= mark_det


#Print the output dictionary.
print("\n'Roll no.' | 'Marks' ")
for key,value in student_marks.items():
    print(key, ':- ')

    for k,v in value.items():
        print('\t   ',k, ': ',v)
    print()

print()
