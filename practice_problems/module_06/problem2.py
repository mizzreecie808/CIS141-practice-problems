# Module 06 - Problem #2
# Create a list of strings.
# Write code that counts how many times the word "Olympic" appears in the list
# Then print the count.

words = ["France", "Virgin Island", "Olympic", "Congo", "Vanuatu",
"Bosnia", "Olympic", "UAE"]
word_check = "Olympic"
count = 0

for word in words:
    if word == word_check:
        count += 1

print(f"{word_check} was found {count} times in the list.")
