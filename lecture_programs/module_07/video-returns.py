# Returns
# https://www.youtube.com/watch?v=MddybWTSJAE

# By default functions return nothing
def print_message():
    # printing something to the console is a side effect
    print("This function doesn't return a value.")
# result = print_message()
# print(result)  # None

# Use return keyword to return something
def cis_faculty_advisor(discipline):
    if discipline == "programming":
        # tuple, similar to list but its immuatable, can't change
        return "Lindsey Handley", "Stephen Foster"
    elif discipline == "security":
        return "Kevin Blackwell"
    elif discipline == "web":
        return "Peter Bill"
    else:
        return "Richard Becker"


def print_advisor(result):
    if(type(result) == tuple):
        advisor1, advisor2 = result
        print(advisor1)
        print(advisor2)
    else:
        print(result)

# Returning multiple values
disciplines = ["programming","security","web"]
for d in disciplines:
    result = cis_faculty_advisor(d)
    print(f"---{d.capitalize()}---")
    print_advisor(result)
    print()

# result = cis_faculty_advisor("programming")
# print_advisor(result)


