"""
In this challenge, we will determine if one number is twice as large as another 
number. To do this, we will compare the first number with two times the second 
number. Here are the steps:

	1.	Define our function with two inputs num1 and num2

	2.	Multiply the second input by 2

	3.	Use an if statement to compare the result of the last calculation with the 
		first input

	4. 	If num1 is greater then return True otherwise return False
"""
# Write your twice_as_large function here:
def twice_as_large(num1, num2):
	if num1 > (2*num2):
		return True
	else:
		return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True