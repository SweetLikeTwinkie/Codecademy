"""
Next, we are going to try something a bit different. This time we are going to
count the number of occurrences of a certain letter within a string. Our function
will accept a parameter for a string and another for the character which we are
going to count. For example, providing the word "mississippi" and the character
's' would result in an answer of 4. These are the steps we need to take:

    1.  Define the function to accept two parameters. word for the input string and x
        for the single character

    2.  Create a counter to keep track of the occurrences

    3.  Loop through every letter in the string. If the current letter is equal to the
        input letter, increase our counter

    4.  Return the counter after looping through the entire string.
"""


# Write your count_char_x function here:
def count_char_x(word, x):
    occurrences = 0
    for letter in word:
        if letter == x:
            occurrences += 1
    return occurrences


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
