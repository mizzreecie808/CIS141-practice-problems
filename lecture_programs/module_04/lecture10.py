# Problem #10: Park Pass Eligibility

age = int(input("How old are you? "))
student = input("Are you an OC student? (True/False) ")

if age < 12 or age >= 65 or student.lower() == "true":
    print("You are eligible for a discount")
else:
    print("Sorry no discount")
