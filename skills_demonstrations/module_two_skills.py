#Module Two Skills Demonstration
#Ask user for their name
user_name = input("Hello, what is your name?") + ","
#print(user_name)

#Ask user for total bill amount
total_bill = int(input("What is the bill amount?"))
#print(total_bill)

#Ask user for number of people splitting bill
people = int(input("How many people in your party?"))
#print(people)

#Calculate how much each person should pay
split_amount = total_bill / people
split_amount = "$" + str(split_amount)

#Display result with friendly message
print(user_name, "each person in your party will pay", split_amount, "Thank you!")