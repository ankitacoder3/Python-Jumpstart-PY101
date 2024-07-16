'''
Problem Statement:
a)	Given s=‘mohanDas Karamchand gandhi'  print:  
        i) m K gandhi  ii) M K GANDHI  iii) M K Gandhi   iv) Mohandas Karamchand Gandhi
b)	Given s = "bad python bad teacher bad lecture"
        i)	Replace all occurrences of bad to good
        ii)	Replace first occurrence of bad to good
        iii)	find the leftmost bad
        iv)	find the second bad from left
        v)	Replace the second bad to worst and display from that point of string and also display the whole string
'''
print('\nCalculate List_string_operations.py\n')

#"answer A"
print('PART A :- \n')

#(string0) string, given as input 
string0='mohanDas Karamchand gandhi'
print("\n The input string is:\t", string0)
print()

#splitting the input string and getting a new list(string1)
string1=string0.split(" ")

#converting list obtained by splitting into string, using join function
string2=' '.join(string1)

#converting all characters to upper case(string2), using the upper function and splitting it
string2= str.upper(string2)
string2= string2.split(" ")

#converting list obtained by splitting into string, using join function
string3=' '.join(string2)

#converting all characters to lower case(string3), using the lower function and splitting it
string3= str.lower(string3)
string3= string3.split(" ")


#using a combination of string1, string2, string3, alongwith concatenation(+) to give the following results, as output.

#part i ans
print("\n  Ans(i):\t", string1[0][0], string1[1][0], string1[2])

#part ii ans
print("\n  Ans(ii):\t", string2[0][0], string2[1][0], string2[2])


#part iii ans
print("\n  Ans(iii):\t", string2[0][0], string1[1][0], string2[2][0]+string1[2][1:6])


#part iv ans
print("\n  Ans(iv):\t", string2[0][0]+string3[0][1:8], string2[1][0]+string1[1][1:10], string2[2][0]+string1[2][1:6])

print()
print()

#"answer B"
print('PART B :- \n')

#(string0) string, given as input 
string0="bad python bad teacher bad lecture"
print("\n The input string is:\t", string0)
print()

#using replace function to get the following results, for (i) and (ii), and printing the output.

#part i ans
replace= string0.replace('bad','good')
print("\n  Ans(i): Replacing all occurences of 'bad' with 'good' -\n\t", replace)

#part ii ans
replace= string0.replace('bad','good',1)
print("\n  Ans(ii): Replacing first occurence of 'bad' with 'good' -\n\t", replace)


#using find function to get the following results, for (iii) and (iv), and printing the output.

#part iii ans
find= string0.find('bad')
print("\n  Ans(iii): Finding the leftmost or first occurence of 'bad' is at -\n\t Index",find)

#part iv ans
find= string0.find('bad',4,16)
print("\n  Ans(iv): Finding the second occurence (from left) of 'bad' is at -\n\t Index",find)


#using a combination of find function, replace function,slicing and concatenation, to get the following result for (v), and printing the output.

#part v ans
replace1= string0[find:].replace('bad','worst',1)
replace2= replace[0:12] + replace1

print("\n  Ans(v): 1- Replacing the second occurence (from left) from 'bad' to \n\t'worst', and printing the string from that point -\n\t\t",replace1)
print("\n  Ans(v): 2- Replacing the second occurence (from left) from 'bad' to \n\t'worst', and printing the string from the beggining -\n\t\t",replace2)

print()