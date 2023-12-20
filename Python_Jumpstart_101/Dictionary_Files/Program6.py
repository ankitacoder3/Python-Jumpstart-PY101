'''
Problem Statement:
In the given dictionary form a new dictionary with srn as key and value as total marks and percentage
Marks={'PECS001': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 'PECS015': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84},
    'PECS065': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 'PECS035': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84},
    'PECS038': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}}
'''

#Giving input dictionary.

Marks={'PECS001': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 'PECS015': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 'PECS065': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 'PECS035': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}, 'PECS038': {'phy': 79, 'chem': 99, 'mat': 84, 'Bio': 84}}

#Making 2 new empty dictionaries.
new_dictionary={}
score={}

#Using 'for' loop, to get srn as key, and total_marks,percentage as values.
for K,v in Marks.items():
    new_dictionary['total marks']=sum(v.values())
    new_dictionary['percentage']= new_dictionary['total marks']/4
    score[K]=new_dictionary


#Print the output dictionary.
print(score)
