'''
Problem Statement:
Use callback to find sum,
double and triple the given number.
'''
print('\nCalculate Callbacks.py\n')

#Defining the 4 functionS. 

def Sum(a):
    s=0
    for i in range(1,a+1):
        s+=i
    print('\tThe SUM of 0 to',a,'is -> ',s)

def Double(a):
    print('\tThe DOUBLE of',a,'is -> ',a*2)

def Triple(a):
    print('\tThe TRIPLE of',a,'is -> ', a*3)

def function(i,func):
    func(i)


#Getting the input, a number.
number= int(input('Enter a number: '))

#Printing the output, by calling the function (by using 'callback concept').
print('\nResult: ')

function(number,Sum)
function(number,Double)
function(number,Triple)
print('\n')
