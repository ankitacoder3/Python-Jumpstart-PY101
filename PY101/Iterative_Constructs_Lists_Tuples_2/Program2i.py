'''
Problem Statement:
Print the given data in the string as formal letter, with one sentence in each line.
s='Respected sir,\n I am here by enlisting all the programming languages
we teach.\n Problem solving using python.\n Object oriented programming
with C++\n Java and jee. \n R programming. \n Thanking You \n Team Programming Languages '
'''
print('\nCalculate Formal_letter.py\n')

#input for formal letter
Letter = 'Respected sir,\n \n I am here by enlisting all the programming languages we teach:\n Problem solving using python\n Object oriented programming with C++\n Java and jee \n R programming \n  \n Thanking You, \n Team Programming Languages.'
print('Input (without using loops):\n',Letter)

#splitting the lines in the Letter
Letter= Letter.split('\n')

#using the for loop to print the output.
print('\nOutput letter (using loops):\n')
for l in Letter:
    print(l)
print()