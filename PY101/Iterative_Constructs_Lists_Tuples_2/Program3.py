'''
Problem Statement:
a)  given list of captains and teams(in respective order) assign them to IPL Teams.
    number_list = ['Kohli','Dhoni','RohitS']
    str_list = ['RCB', 'CSK', 'MI']
b)  Given list of tuples, where each tuple takes pattern (name,marks) of a student, display only names.
'''

#"answer A"

#2 Lists (one of captains and one of teams), given as input 
captain_list=['Virat Kohli','MS Dhoni','Rohit Sharma']
team_list=['RCB', 'CSK', 'MI']
print("Answer (a)")
print("\n The input list for captains is:\n\t", captain_list)
print("\n The input list for teams is:\n\t", team_list)
print()


#using the zip function to match the captains to their teams 
result=zip(captain_list,team_list)
result=list(result)

#printing the output
print(" Output/Result: \n  The list of captains and teams are as follows:\n\t", result)
print()
print()


#"answer B"

#1 List (containing both student names and marks, in tuple form), given as input 
sample=[("Riya",100),("Lily",99),("Tara",97),("Rajesh",95),("Rohan",93),("Ritu",95),("James",93)]
print("Answer (b): \n \n The input list is:\n", sample)
print()

#using the zip(*) function unzip the given list. 
result1=zip(*sample)
result1=list(result1)

#printing the output
print(" \n 'Process:'\n ' The list after unzipping the input list: '\n ", result1)
print(" \n \n Output/Result: \n  The list of only names:\n\t", result1[0])



