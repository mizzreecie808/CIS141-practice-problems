# ChatGPT 🧠 Dictionaries
# 🔹 Problem 3: Word Frequency Counter
# key-value, "word" : count, "the" : 3

word_count = {}
sentence = "the quick brown fox jumps over the lazy dog and the quick blue hare"

for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

