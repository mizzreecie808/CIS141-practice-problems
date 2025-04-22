'''
Problem #4
Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user
Print to the screen.
'''

# user input for word, first and last index
word = input("What word would you like to slice? ")
first, last = int(input("First slice? ")), int(input("Last slice? "))

# slice the word
sliced = word[first:last]

# print the sliced word
print(f"Your sliced word at index {first} and {last} is: {sliced}")
