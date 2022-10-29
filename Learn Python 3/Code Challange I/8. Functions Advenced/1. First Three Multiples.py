"""
Let’s start by creating a function which both prints and returns values. For this 
function, we are going to print out the first three multiples of a number and 
return the third multiple. This means that we are going to print 1, 2, and 3 times 
the input number and then return the value of 3 times the input number. For this, 
we are going to need a few steps:

	1.	Define the function header to accept one input parameter called num

	2.	Print out 1 times num

	3.	Print out 2 times num

	4.	Print out 3 times num

	5.	Return the value of 3 times num
"""
# Write your first_three_multiples function here
def first_three_multiples(num):
	print(num)
	print(num * 2)
	print(num * 3)
	return num * 3
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0