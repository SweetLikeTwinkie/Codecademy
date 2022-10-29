"""
For the final challenge in this group, we are going to take the remainder of two 
numbers while performing other mathematical operations on them. We are going 
to multiply the numerator by 2 and divide the denominator by 2. After the two 
values have been modified, we will divide them and return the remainder. In 
order to do this we will need to:

	1.	Define the function to accept two parameters

	2.	Multiply the first input value by 2

	3.	Divide the second input value by 2

	4.	Calculate the remainder of the modified first input value divided by the 
		modified second input value (using modulus)

	5.	Return the answer
"""
# Write your remainder function here:
def remainder(num1, num2):
	return (2 * num1) % (num2 / 2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0