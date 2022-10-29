"""
There are some situations that you normally want to avoid when programming 
using conditional statements. One example is a contradiction. This occurs when 
your condition will always be false no matter what value you pass into it. Let’s 
create an example of a function that contains a contradiction. It will contain a 
few steps:

	1.	Define the function to accept a single parameter called num

	2.	Use a combination of <, > and and to create a contradiction in an if 
		statement.

	3. 	If the condition is true, return True, otherwise return False. The trick here is 
		that because we’ve written a contradiction, the condition should never be 
		true, so we should expect to always return False.
"""
# Write your always_false function here:
def always_false(num):
	if (num > 0  and num < 0):
		return True
	else:
		return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False