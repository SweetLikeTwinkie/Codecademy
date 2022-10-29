"""
For the final challenge, we are going to test two lists to see if the second list is the 
reverse of the first list. There are a few different ways to approach this, but we 
are going to try a method that iterates through each of the values in one 
direction for the first list and compares them against the values starting from the 
other direction in the second list. Here is what you need to do:

	1.	Define a function that has two input parameters for our lists

	2.	Loop through every index in one of the lists from beginning to end

	3.	Within the loop, compare the element in the first list at the current index 
		against the element at the second list’s last index minus the current index. If 
		there was a mismatch, then the lists aren’t reversed and we can return False
	
	4.	If the loop ended successfully, then we know the lists are reversed and we can 
		return True.
"""
#Write your function here
def reversed_list(lst1, lst2):
	for index in range(len(lst1)):
		if lst1[index] != lst2[len(lst2) - 1 - index]:
			return False
	return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))