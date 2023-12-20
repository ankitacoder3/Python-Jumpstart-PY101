'''
Problem Statement:
Separate the following list to different lists based on following criteria:
i)	Starts with 'pizza' 
ii)	Ends with 'puri' 
iii)	Ends with 'dosa'
Input: l=['pani puri','dosa','bhel puri','masala dosa','dahi puri','rava dosa','pizza topings','pizza mania']
'''

#defining the main list
main_list=['pani puri','dosa','bhel puri','masala dosa','dahi puri','rava dosa','pizza toppings','pizza mania']
print(f"The main input list, that has to be classified is:")
print(main_list)
print(' ')

#making three empty lists, based on the criteria given in the question.
starts_pizza =[]
ends_puri =[]
ends_dosa =[]


#to classify the item in the main list into the 3 new lists
#by using the for loop, if condition and elif condition

for item in main_list:
    if item.startswith('pizza'):
        starts_pizza.append(item)
    elif item.endswith('puri'):
        ends_puri.append(item)
    elif item.endswith('dosa'):
        ends_dosa.append(item)

#output
print (f"The list that 'starts' with 'PIZZA' is:  {starts_pizza}")
print (f"The list that 'ends' with 'PURI' is:  {ends_puri}")
print (f"The list that 'ends' with 'DOSA' is:  {ends_dosa}")
