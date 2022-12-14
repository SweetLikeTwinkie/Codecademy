"""
Let’s start our challenging problems with a function that creates a list of numbers 
up to 100 in increments of 3 starting from a number that is passed to the function 
as an input parameter. Here is what we need to do:

	1.	Define the function to accept one parameter for our starting number

	2.	Calculate the numbers between the starting number and 100 while 
		incrementing by 3

	3.	Store the numbers in a list

	4.	Return the list
"""
#Write your function here
def every_three_nums(start):
	return list(range(start,101,3))
#Uncomment the line below when your function is done
print(every_three_nums(91))