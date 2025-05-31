# Module 08 Lecture Problems
# 05: Olympic College Club Tracker
file_name = "clubs.txt"
with open(file_name, "a") as file:
    new_club = input("What is the name of the club you joined? ")
    file.write(new_club + "\n")

count = 1
with open(file_name, "r") as file:
    print("List of College Clubs:")
    print("=" * 22)
    for line in file:
        print(f"{count}: {line.strip()}")
        count += 1
