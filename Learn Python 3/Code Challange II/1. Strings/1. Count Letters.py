"""
For the first code challenge, we are going to count the number of unique letters 
in a string. This means that when we are looking at the word, any new letters 
should be counted and any duplicates should not be counted. There are a few 
ways to solve this, but we can use the provided alphabet string to ensure that 
duplicates are not counted. Here is what we need to do:

	1.	Define the function to accept one parameter — the word whose letters we 
		are counting

	2.	Create a counter to keep track of unique letters

	3.	Loop through every letter in our alphabet string. If the current letter was 
		found in our word, increase our count

	4.	Return the count after looping through all letters.
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Write your unique_english_letters function here:
def unique_english_letters(word):
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
