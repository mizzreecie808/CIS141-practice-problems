# Module 08 - Problem #2
# Write a Python program that allows users to log their hiking trips.
# - Use a while loop to repeatedly ask for a hike name and distance in miles
# - Save each entry to hiking_log.txt (each hike on a new line)
# - When the user presses 0, exit the loop & print contents of hiking_log.txt

# module that takes variable of a file name
def log_hike(file_name):
    while True:
        user_input = input("What is the hike name and distance? ")

        messages = [
            "Thank you for logging your hikes!",
            "Please ensure you entered hike name and distance.",
            "You only entered hike name, not the distance."
        ]

        output = validate_input(user_input)

        if output == 0:
            print(messages[0])
            # calls the module to print the log to console
            print_log(file_name)
            break
        elif output == 1:
            print(messages[1])
            continue
        elif output == 2:
            print(messages[2])
            continue
        else:
            with open(file_name, "a") as file:
                file.write(f"{user_input}\n")

# module to print the contents of a text file to the console
def print_log(file_name):
    print(f"\nHiking Log\n{'='*22}")
    with open(file_name, "r") as file:
        for hike in file:
            print(hike.strip())

# module validates user input
# checks for "0" to exit
# ensures user inputs a name and a distance
# ensures distance entered is entered correctly
def validate_input(user):
    if user == "0":
        return 0

    if len(user.split()) < 2:
        return 1

    last_word = user[-1]
    check_int = last_word.isdigit()
    check_float = last_word.count(".") == 1 and last_word.replace(".","").isdigit()

    if not check_int and not check_float:
        return 2
    else:
        return 3

hikes = "hiking_log.txt"
log_hike(hikes)
