"""
Let’s say we are working with two conveyor belts that contain items represented 
by a numerical ID. If one conveyor belt contains more items than the other, then 
we need to return the ID of the last item on that belt. In the case where they have 
the same number of items, return the last item from the first conveyor belt. In 
our code, we can represent the belts using lists. Here are the steps:

	1.	Define the function to accept two parameters for our two lists of numbers

	2.	Check if the length of the first list is greater than or equal to the 
		length of the second list

	3.	If true, then return the last element from the first list. Otherwise, return the 
		last element from the second list
"""
#Write your function here
def larger_list(lst1, lst2):
	if (len(lst1) >= len(lst2)):
		return lst1[-1]
	else:
		return lst2[-1]
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))