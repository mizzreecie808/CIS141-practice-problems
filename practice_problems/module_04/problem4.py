'''
Problem #4
Ask the user for their age tell them whether they can see:
G     (appropriate for under 13)
PG-13 (appropriate for 13 to 17)
R     (appropriate for over 18) rated movies
'''

age = int(input("How old are you? "))

if age > 18:
    print("You can watch G, PG-13 and R rated movies.")
elif 13 < age < 17:
    print("You can watch G and PG-13 rated movies.")
else:
    print("You can only watch G rated movies.")


# Problem 4: you're currently skipping logic for ages 13 & 17.
# Consider what should happen if someone inputs 13 or 17.
# I added in the ">=" symbol for the if and elif statements.
# This will allow for inputs of exactly 13, 17 and 18

age = int(input("How old are you? "))

if age >= 18:
    print("You can watch G, PG-13 and R rated movies.")
elif 13 <= age <= 17:
    print("You can watch G and PG-13 rated movies.")
else:
    print("You can only watch G rated movies.")
