'''
Problem Statement:
Use callback to find sum,
double and triple the given number.
'''

#Defining the 4 functionS. 

def Sum(a):
    s=0
    for i in range(1,a+1):
        s+=i
    print('The SUM is: ',s)

def Double(a):
    print('The DOUBLE of ',a,' is: ',a*2)

def Triple(a):
    print('The TRIPLE of ',a,' is: ', a*3)

def function(i,func):
    func(i)


#Getting the input, a number.
number= int(input('\nEnter a number:'))
print('\n')

#Printing the output, by calling the function (by using 'callback concept').
function(number,Sum)
function(number,Double)
function(number,Triple)
print('\n')
