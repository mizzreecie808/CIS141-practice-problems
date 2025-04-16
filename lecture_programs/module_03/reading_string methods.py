# Reading - Strings Methods in Python
# Testing Strings
#print("byte".isalnum())
#print("byte".isalpha())
#print("123".isdigit())
#print("123".islower())
#print("AAA".isupper())
#print("AAA".isspace())

# Searching
#print("abc".endswith("bc")) #boolean
#print("python".startswith("pyt")) #boolean
#print("Learning".find("n")) #returns index of character, -1 if not found
#print("Learning".rfind("n")) #returns highest index of character, -1 if not found
#print("Mississippi".count("s")) #counts that character(s)

# Replacing
str1 = "Learning C" #old string
#print(id(str1))
str2 = str1.replace("C", "Python") #creates new string
#print(id(str2))
#print(id(str1))

# Converting Strings
#print("abcDEF".lower())
#print("abcDEF".upper())
#print("a long string".capitalize())
#print("a long string".title())
#print("ABCdef".swapcase())
str3 = "\n\tName\tAge"
#print(str3)
str4 = str3.strip()
#print(str4)

# Formatting Methods
print("NAME".center(20))
print("Justified Left".ljust(10))
print("Justified Right".rjust(5))
