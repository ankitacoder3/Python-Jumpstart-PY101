'''
Problem Statement:
Solve tower of Hanoi problem.
'''
print('\nCalculate Tower_of_hanoi.py\n')

#Defining tower of hanoi function.

def TowerOfHanoi(z,source,destination,auxillary):
    if z==1:
        print(f"\tMove 'ring-1' from '{source}' peg to '{destination}' peg.")
        return
    TowerOfHanoi(z-1,source,auxillary,destination)
    print(f"\tMove 'ring-{z}' from '{source}' peg to '{destination}' peg.")
    TowerOfHanoi(z-1,auxillary,destination,source)
            

#Getting input, for number of discs.
number= int(input('Enter number of discs: '))
print("\nGiven as input:- \n \t\t Source peg is 'start(A)' \n \t\t Destination peg is 'stop(B)' \n \t\t Auxillarypeg is 'middle(C)' \n ")

#Printing the output, by calling the function.
print("Result:- ")
TowerOfHanoi(number,'start(A)','stop(B)','middle(C)')

print()