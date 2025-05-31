# Module 08 Lecture Problems
# 04: Kitsap County Visitor Log
file_name = "visitor_log.txt"
user_name = input("What is your name? ").capitalize()
destination = input("What is your favorite Kitsap County destination? ").capitalize()

with open(file_name, "a") as file:
    new_line = f"{user_name}: {destination}"
    file.write(new_line)
