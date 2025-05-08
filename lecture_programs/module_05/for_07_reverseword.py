# ChatGPT 🔁 For Loop Practice
# 7. Reverse Word: print user word in reverse
word = "Hello"
print(f"'{word}' printed forward: ")
for letter in word:
    print(letter, end = " ")
print()

print(f"'{word}' printed backward: ")
for letter in reversed(word):
    print(letter, end = " ")
print()

print(f"'{word}' printed backward, using slicing: ")
for letter in word[::-1]:
    print(letter, end = " ")
print()
