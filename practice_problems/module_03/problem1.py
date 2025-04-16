'''
Problem #1
Prompt the user for a word.
Then, prompt the user for how many times they'd like that word repeated.
Print the word the correct number of times.
'''

# prompt user for word
word = input("Please type in a word of your choice.\t")

# prompt for times to repeat, must change type to int
repeat = int(input("Now tell me how many times you want to repeat this word.\t"))

# this will print all words joined on one line
print(word * repeat)

# this will print the word on new lines
print((word + "\n") * repeat)

# this will print the word with space (or character of chosing) between each
print((word + " ") * repeat)
