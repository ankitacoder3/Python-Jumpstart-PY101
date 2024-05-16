'''
Problem Statement:
Solve tower of Hanoi problem.
'''

#Defining tower of hanoi function.

def TowerOfHanoi(z,source,destination,auxillary):
    if z==1:
        print(f"Move 'ring-1' from '{source}' peg to '{destination}' peg.")
        return
    TowerOfHanoi(z-1,source,auxillary,destination)
    print(f"Move 'ring-{z}' from '{source}' peg to '{destination}' peg.")
    TowerOfHanoi(z-1,auxillary,destination,source)
            

#Getting input, for number of discs.
number= int(input('\nEnter number of discs:'))

#Printing the output, by calling the function.
print("\nGiven as input:- \n \t Source peg is 'start(A)' \n \t Destination peg is 'stop(B)' \n \t Auxillarypeg is 'middle(C)' \n ")
TowerOfHanoi(number,'start(A)','stop(B)','middle(C)')

print()
