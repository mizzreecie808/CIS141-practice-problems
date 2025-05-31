# Dictionaries
# https://www.youtube.com/watch?v=SPUukIIOBpY
# key-value pairs, seperated by ':'
# name - Jenny = key, number = value

contacts = {
    "Jenny": "867-5309",
    "Bobby": "111-222-3333",
    "Lindsey": "111-222-3311"
}

# print(contacts)
# print(contacts["Jenny"])

# Adding a new key-value pair to dictionary
contacts["Cerise"] = "360-689-4742"
# print(contacts)
# print(contacts["Cerise"])

# Checking to see if value exists in dictionary
# if "Jose" in contacts:
#     print("Jose's contact is:", contacts["Jose"])
# else:
#     print("Does not exist")

# From TIOBE index
language_rankings = {
    "Python": 1,
    "C++": 2,
    "Java": 3
}

print(language_rankings["Python"])  # prints Python ranking
language_rankings["Ruby"] = 19
print(language_rankings)
