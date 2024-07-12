'''
Problem Statement:
In the given dictionary form a new dictionary with SRN as key and value as total marks and percentage
Marks={'PECS001': {'phy': 79, 'chem': 90, 'mat': 84, 'Bio': 94}, 'PECS015': {'phy': 70, 'chem': 99, 'mat': 85, 'Bio': 80}, 
    'PECS065': {'phy': 79, 'chem': 59, 'mat': 54, 'Bio': 88}, 'PECS035': {'phy': 70, 'chem': 90, 'mat': 84, 'Bio': 84}, 
    'PECS038': {'phy': 55, 'chem': 66, 'mat': 88, 'Bio': 81}}
'''
print('\nCalculate Total_marks_percentage.py\n')

print('Dictionary where the keys are SRN, and the values are the respective total marks and percentages. ')

#Giving input dictionary.
Marks={
    'PECS001': {'phy': 79, 'chem': 90, 'mat': 84, 'Bio': 94}, 
    'PECS015': {'phy': 70, 'chem': 99, 'mat': 85, 'Bio': 80}, 
    'PECS065': {'phy': 79, 'chem': 59, 'mat': 54, 'Bio': 88}, 
    'PECS035': {'phy': 70, 'chem': 90, 'mat': 84, 'Bio': 84}, 
    'PECS038': {'phy': 55, 'chem': 66, 'mat': 88, 'Bio': 81}
    }

#Making 2 new empty dictionaries.
score={}
new_dictionary={}


#Using 'for' loop, to get srn as key, and total_marks,percentage as values.
for K,v in Marks.items():
    new_dictionary['Total Marks']=sum(v.values())
    new_dictionary['Avg Percentage']= new_dictionary['Total Marks']/4 
    score[K]=new_dictionary
    new_dictionary={} #resetting values in dictionary


#Print the output dictionary.
print("\n'Roll no.' | 'Details' ")
for key,value in score.items():
    print(key, ':- ')

    for k,v in value.items():
        print('\t    ',k, ': ',v)
    print()

print()