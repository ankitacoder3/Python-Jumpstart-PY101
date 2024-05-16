'''
Problem Statement:
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the rest copy and 75 cents for each additional copy.
What is the total wholesale cost for 60 copies?
'''

#getting input for the total no. of books to be shipped.
n= int(input("total no. of books to be shipped:"))

#calculating the discount and the total cost.
discount = (24.95*n)*( 40/100)
total_cost = (3*discount)+((0.75*discount)*(n-1))
total_cost= round(total_cost, 8)

#output
print("The total cost for shipping {} number of books is {} dollars.". format (n, total_cost))


