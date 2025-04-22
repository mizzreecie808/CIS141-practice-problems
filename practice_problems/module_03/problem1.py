'''
Problem #1
Prompt user for a word.
Prompt user for times they'd like that word repeated.
Print the word the correct number of times.
'''

# prompt user for word
word = input("Please type in a word of your choice. ")

# prompt for times to repeat, must change type to int
repeat = int(input("How many times you want to repeat this word. "))

# this will print all words joined on one line
print(word * repeat)

# this will print the word on new lines
print((word + "\n") * repeat)

# this will print the word with space (or character of chosing) between each
print((word + " ") * repeat)
