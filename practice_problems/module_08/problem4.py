# Module 08 - Problem #4
# Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas
# Write a program that reads the poll.txt file
# Count how many votes "yea" or "nay" received and print the results.

file_name = "poll.txt"
votes = {"yea": 0, "nay": 0}

with open(file_name, "r") as file:

    for line in file:

        words = line.strip().lower().replace(",","").split()

        for word in words:
            if word == "yea":
                votes["yea"] += 1
            elif word == "nay":
                votes["nay"] += 1
            else:
                print("Neither yea nor nay")

print("Voting Results")
print("-"*14)
for key, value in votes.items():
    print(f"{key}: {value}")
