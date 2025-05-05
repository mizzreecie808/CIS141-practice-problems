# Advanced String Concepts
# https://www.youtube.com/watch?v=WipXWAPaTmY

# Strings are Objects
text = "hello world"
#print(text.upper())
#print(text.capitalize())
#print(text.lower())

# Immutability: Strings Cannot Change in Place
new_text = "y" + text[1:]
print(new_text)

# Comparision with Mutable Sequences ex. List
my_list = [1, 2, 3]
my_list[0] = "A"
print(my_list)

# .replace(), .split(), and .join()
phrase = "banana"
new_phrase = phrase.replace("na", "NA")
print(phrase, new_phrase)

phrase2 = "Hello my name is Cerise"
split_phrase = phrase2.split(" ")
print(split_phrase)

join_phrase = "|".join(split_phrase)
print(join_phrase)

# print() end & sep keyword args
# sep is a keyword to use to identify a difference seperator
print(text, phrase, phrase2, sep ="; ", end="!!!!!\n")
