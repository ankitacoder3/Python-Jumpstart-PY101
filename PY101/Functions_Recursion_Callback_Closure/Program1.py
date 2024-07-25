'''
Problem Statement:
Using Functions generate prime numbers,
using method of Sieve of eratosthenes.
'''
print('\nCalculate Sieve_of_eratosthenes.py\n')


#Defining Sieve of eratosthenes function.

def Sieve_eratosthenes(n):
	prime = [True for i in range(n+1)]	# boolean array
	p = 2
	while (p * p <= n):

		# If prime[p] is not
		# changed, then it is a prime
		if (prime[p] == True):

			# Updating all multiples of p
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1

	# Print all prime numbers
	for p in range(2, n+1):
		if prime[p]:
			print('   ',p,end="\t")

#Getting input, for a number.
number = int(input('\n  Enter a number: '))

#Printing the output, by calling the function.
print(f'\n  Prime numbers smaller than or equal to \'{number}\' are:\n')
Sieve_eratosthenes(number)
print()
print()

print()