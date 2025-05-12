# ChatGPT 🔁 Challenge 3: Password Retry (while loop)
# While loop that keeps asking for user password "secret123"
# If wrong, print "Wrong password, try again."
# If correct, print "Access granted!"

user_input = input("Password: ")

while user_input != "secret123":
    print("Wrong password, try again")
    user_input = input("Password: ")

print("Access granted!")
