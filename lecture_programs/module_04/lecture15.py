# Problem #15: Scholarship Eligibility at OC

gpa = float(input("What is your GPA? "))
credits = int(input("How may credits have you completed? "))
is_cs_major = input("Are you a CS/CIS major? (True/False) ").strip().lower() == "true"

# my first try
# if gpa and credits and cs_major:
#     print("The Tech Titans scholarship is yours!")
# elif gpa and credits and not cs_major:
#     print("Sorry - You're not a CS/CIS Major")
# elif gpa and not credits and cs_major:
#     print("Sorry - You don't have enough credits")
# elif not gpa and credits and cs_major:
#     print("Sorry - Your GPA isn't high enough")
# elif gpa and not credits and not cs_major:
#     print("Sorry - You're not a CS/CIS Major and you don't have enough credits")
# elif not gpa and credits and not cs_major:
#     print("Sorry - Your GPA isn't high enough and you're not a CS/CIS Major")
# elif not gpa and not credits and cs_major:
#     print("Sorry - Your GPA isn't high enough and you don't have enough credits")
# else:
#     print("Sorry - Your GPA isn't high enough, you don't have enough credits and you're not a CS/CIS major.")

# cleaner version

meets_gpa = gpa >= 3.5
has_credits = credits >= 45
eligible = meets_gpa and has_credits and is_cs_major

if eligible:
    print("The Tech Titans scholarship is yours!")
else:
    print("You didn't get the scholarship because:")
    if not meets_gpa:
        print("- GPA not high enough")
    if not has_credits:
        print("- You don't have enough credits")
    if not is_cs_major:
        print("- You aren't enrolled as a CS/CIS major.")
