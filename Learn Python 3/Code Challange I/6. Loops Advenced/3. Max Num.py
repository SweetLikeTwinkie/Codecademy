"""
Here is a more traditional coding problem for you. This function will be used to 
find the maximum number in a list of numbers. This can be accomplished using 
the max() function in python, but as a challenge, we are going to manually 
implement this function. Here is what we need to do:

	1.	Define the function to accept a list of numbers called nums

	2.	Set our default maximum value to be the first element in the list

	3.	Loop through every number in the list of numbers

	4.	Within the loop, if we find a number greater than our starting maximum, then 
		replace the maximum with what we found.

	5.	Return the maximum number
"""
#Write your function here
def max_num(nums):
	maximum = nums[0]
	for number in nums:
		if number > maximum:
			maximum = number
	return maximum
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))