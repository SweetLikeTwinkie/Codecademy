"""
In this challenge, we need to find the indices in two equally sized lists where the 
numbers match. We will be iterating through both of them at the same time and 
comparing the values, if the numbers are equal, then we record the index. These 
are the steps we need to accomplish this:

	1.	Define our function to accept two lists of numbers

	2.	Create a new list to store our matching indices

	3.	Loop through each index to the end of either of our lists

	4.	Within the loop, check if our first list at the current index is equal to the 
		second list at the current index. If so, append the index where they matched

	5.	Return our list of indices
"""
#Write your function here
def same_values(lst1, lst2):
	new_lst = []
	for index in range(len(lst1)):
		if lst1[index] == lst2[index]:
			new_lst.append(index)
	return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))