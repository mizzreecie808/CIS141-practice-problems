# Problem 1: OC Student Email Check
# Prompt for e-mail address
# Use a boolean to print "You're and OC student!"
# IF it contains "@student.olympic.edu" ELSE
# "Sorry, you're not an OC student."

address = input("What is your e-mail address? ")
must_contain = "@student.olympic.edu"

if must_contain in address:
	print("You're and OC student!")
else:
	print("Sorry, you're not an OC student.")
