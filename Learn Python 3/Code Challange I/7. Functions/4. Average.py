"""
Let’s create a function which takes the average of two numbers. These two 
numbers will be the input of the function and the output will be the average of 
the two. In order to do this, we need to do a few steps:

	1.	Define the function with two input parameters, num1 and num2

	2.	Calculate the sum of the two numbers

	3.	Divide the sum by the number of inputs to the function

	4.	Return the answer
"""
# Write your average function here:
def average(num1, num2):
	return (num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0