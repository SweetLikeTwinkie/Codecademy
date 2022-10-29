"""
Our next function will double a value at a given position. We will provide a list and 
an index to double. This will create a new list by replacing the value at the index 
provided with double the original value. If the index is invalid then we should 
return the original list. Here is what we need to do:

	1.	Define the function to accept two parameters, one for the list and another 
		for the index of the value we are going to double

	2.	Test if the index is invalid. If it’s invalid then return the original list

	3.	If the index is valid then get all values up to the index and store it as a new list

	4.	Append the value at the index times 2 to the new list

	5.	Add the rest of the list from the index onto the new list

	6.	Return the new list
"""
#Write your function here
def double_index(lst,index):
	if index >= len(lst):
		return lst
	else:
		new_lst = lst[0:index]
	new_lst.append(lst[index]*2)
	new_lst = new_lst + lst[index+1:]
	return new_lst
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))