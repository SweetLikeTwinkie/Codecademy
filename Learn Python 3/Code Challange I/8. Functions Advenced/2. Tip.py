"""
Let’s say we are going to a restaurant and we decide to leave a tip. We can create 
a function to easily calculate the amount to tip based on the total cost of the 
food and a percentage. This function will accept both of those values as inputs 
and return the amount of money to tip. In order to do this, we will need a few 
steps:

	1.	Define the function to accept the total cost of the food called total and the 
		percentage to tip as percentage

	2.	Calculate the tip amount by multiplying the total and percentage and dividing 
		by 100

	3.	Return the tip amount
"""
# Write your tip function here:
def tip(total, percentage):
	tip_amount = (total * percentage) / 100
	return tip_amount
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0