# Module 08 Lecture Problems
# 07: Word Counter for Hiking Journal
file_name = "hiking_journal.txt"

with open(file_name, "r") as file:
    word_count = 0

    for line in file:
        words = line.split()

        for word in words:
            word_count += 1

    print(word_count)
