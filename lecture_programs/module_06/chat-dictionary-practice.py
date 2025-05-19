# ChatGPT 👨‍💻 Mini Practice
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# print(person["name"])
# person["age"] += 1
# print(person)

#🧠 Challenge: Build a Contact Book
# Step 1: Create an empty dictionary
contacts = {}

# Step 2: Add 3 contacts
contacts["Alice"] = "555-1234"
contacts["Charlie"] = "555-9876"
contacts["Diana"] = "555-4567"

print(contacts)
# Step 3: Ask user for a name
name = input("Enter a name to look up: ").capitalize()
print(name)

# Step 4 & 5: Check if the name exists
# if name in contacts:
#     print(f"📞 {name}'s number is: {contacts[name]}")
# else:
#     print(f"❌ Sorry, {name} is not in your contacts.")


print(f"{name:<12} 🔢")
