"""
We need to write a program that checks different names and determines if they 
are equal. We need to accept two strings and compare them. Here are the steps:

	1.	Define the function to accept two strings, your_name and my_name

	2.	Test if the two strings are equal
	
	3.	Return True if they are equal, otherwise return False
"""
# Write your same_name function here:
def same_name(your_name, my_name):
	if (your_name == my_name):
		return True
	else:
		return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False