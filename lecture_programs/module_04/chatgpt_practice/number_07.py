# ChatGPT 🌟 Practice Problems - Boolean
# 7. **Username Validation**

username = input("What is your username: ")

if len(username) < 5 or "admin" in username:
    print("Invalid username")
else:
    print("Username accepted!")
