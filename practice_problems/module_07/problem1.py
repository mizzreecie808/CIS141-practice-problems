# Module 07 - Problem #1
# Write a function called count_vowels(input) that takes a string
# and returns the number of vowels (a, e, i, o, u) in it.
# Got practice words from https://www.wordlucky.com/words-with-most/vowels

word1 = "autobiographies"   # 8 vowels
word2 = "baccalaureates"    # 7 vowels

def count_vowels(input):
    count = 0
    for char in input.lower().strip():
        if char in "aieou":
            count += 1
    return count

vowels1 = count_vowels(word1)
print(f"{word1} has {vowels1} vowels")

vowels2 = count_vowels(word2)
print(f"{word2} has {vowels2} vowels")
