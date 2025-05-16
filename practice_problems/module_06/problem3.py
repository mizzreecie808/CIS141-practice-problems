# Module 06 - Problem #3
# Create a list of strings.
# Write code to create a new list that includes only the strings longer
# than three characters.
# Print the resulting filtered list.
words = ["wait", "page", "cat", "parsimonious", "writer", "dog", "cover", "zany"]
longer_words = []

for word in words:
    if len(word) > 3:
        longer_words.append(word)

print(f"Original list:\n  {words}")
print(f"New list, words longer than 3 characters:\n  {longer_words}")
