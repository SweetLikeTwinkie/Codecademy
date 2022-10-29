"""
For the first code challenge, we are going to calculate the length of a list and then 
append the value to the end of the list. Here is what we need to do:

	1.	Define the function to accept one parameter for our list

	2.	Get the length of the list

	3.	Append the length of the list to the end of the list

	4.	Return the modified list
"""
#Write your function here
def append_size(lst):
	lst.append(len(lst))
	return lst
#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))