# Module 08 - Problem #1
# Create a file called gardening_tips.txt
# Reads the file gardening_tips.txt and print each tip one by one

line_count = 0

with open("gardening_tips.txt", "r") as file:
    for line in file:
        # added a line count to number each tip printed
        line_count += 1
        # .strip() will remove the newline and prevent spaces between lines
        print(f"{line_count}: {line.strip()}")

