# Module 08 - Problem #3
# Create a text file called song_lyrics.txt

lyric_count = {}
file_name = "song_lyrics.txt"

# module to get words from user, then store in dictionary "lyric_count"
def get_words(lyric_dict):

    # - Requests 5 inputs from user : 5 words to count the frequency of
    count = 1
    while count <= 5:
        user_word = input(f"Enter word #{count}: ").strip().lower()

        # check if user inputted more than one word
        if len(user_word.split()) > 1:
            print("Only one word please.")
            continue

        # check if word is already in the dictionary
        if user_word in lyric_dict:
            print("You already picked that word.")
            continue

        # - Creates a dictionary of the words and their counts
        count += 1
        lyric_dict[user_word] = 0

    # - Print the dictionary to the console
    print("Here are the words you want to count:")
    print("-" * 37)
    for item in lyric_dict:
        print(item)

def count_words(song, lyric_dict):

    # - Reads the file
    with open(song, "r") as file:

        # first read each line
        for line in file:

            # second split the line into words, remove "," & change to lowercase
            words = line.strip().lower().replace(",","").split()

            # - Counts how many times each word appears
            # third count each word and match against the dictionary
            for word in words:
                if word in lyric_dict:
                    lyric_dict[word] += 1

    # - Print the dictionary to the console

    print("Here are the totals of each word:")
    print("-" * 33)
    for key, value in lyric_dict.items():
        print(f"{key}:\t{value}")


get_words(lyric_count)
count_words(file_name, lyric_count)
