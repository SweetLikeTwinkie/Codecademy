"""
Let’s go back to our factory example. We have a conveyor belt of items where 
each item is represented by a different number. We want to know, out of two 
items, which one shows up more on our belt. To solve this, we can use a function 
with three parameters. One parameter for the list of items, another for the first 
item we are comparing, and another for the second item. Here are the steps:

	1.	Define the function to accept three parameters: the list, the first item, and 
		the second item

	2.	Count the number of times item1 shows up in our list

	3.	Count the number of times item2 shows up in our list

	4.	Return the item that appears more frequently in lst — if both items show up 
		the same number of times, return item1
"""
#Write your function here
def more_frequent_item(lst,item1,item2):
	if lst.count(item1) >= lst.count(item2):
		return item1
	else:
		return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))