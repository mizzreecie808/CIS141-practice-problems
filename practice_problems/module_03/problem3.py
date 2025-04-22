'''
Problem #3
Prompt the user for a sentence and a word to try to find in that sentence.
Have the program print out whether the word was found in the sentence.
(i.e. True or False)
'''
sentence = input("Please type a sentence. ")
word = input("Choose a word to find. ")

# if the word is found in the sentence, it will return a number that represents
# the starting index of that word, if the word is not found, it will return -1
found = sentence.find(word) != -1

print(f"Is the word: ({word}) in the following sentence: ({sentence})?\n{found}")
