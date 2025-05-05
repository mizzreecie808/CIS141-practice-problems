# ChatGPT 🌟 Practice Problems - Boolean
# Mini-Challenge #3: Class Enrollment
# Rules - all have to be true for them to enroll
# completed_prereq (yes/no)
# has_sched_conflict (yes/no)
# class_full (yes/no)
completed_prereq = input("Have you completed the prerequisite? (yes/no) ")
has_sched_conflict = input("Are there any schedule conflicts? (yes/no) ")
class_full = input("Is the class full? (yes/no) ")
gpa = float(input("What is your gpa? "))
is_honors_class = input("Is this an honors class? (yes/no) ")

if completed_prereq.lower() == "yes" and has_sched_conflict.lower() == "no" and class_full.lower() == "no":
    if is_honors_class.lower() == "yes" and gpa > 3.5:
        print("You are eligible to enroll in this honors class!")
    if is_honors_class.lower() == "no":
        print("You are eligible to enroll in this regular class!")
else:
    print("You are not eligible to enroll!")
