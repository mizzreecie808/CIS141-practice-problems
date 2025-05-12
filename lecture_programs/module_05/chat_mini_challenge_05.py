# ChatGPT 🎲 Challenge 5: Word Pyramid
# User input to get a word
# Build pyramid like this
# c     row 1
# co    row 2
# cod   row 3
# code  row 4

user_input = input("Select a word: ")

# use a loop to go through each character index

for i in range(1, len(user_input) + 1):
    # prints from 0 to i
    print(f"[1:{i}]\t{user_input[:i]}")
