'''
Problem Statement:
Write a python program which accepts a sequence of comma-separated values from console and generate as a list and as a tuple. 
'''


#getting input
print("The values should be separated by commas only[no spaces are allowed].")
value = input("Enter the values:")

#splitting the input on the basis of commas, and converting to list and tuple form.
value_list = value.split(",")
value_tuple = tuple(value_list)

#output
print(f"Values in 'Tuple form' ={value_tuple}")
print(f"Values in 'List form' ={value_list}")
