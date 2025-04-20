#Module Two Skills Demonstration
#Ask user for their name
name = input("What is your name? ")

#Ask user for total bill amount
bill = float(input("What is the bill amount? "))

#Ask user for number of people splitting bill
people = int(input("How many people in your party? "))

#Calculate how much each person should pay
each = bill / people

#Format dollar amount to 2 decimal places
each = "$" + format(each, ".2f")

#Display result with friendly message
print(name, "each person must pay", each, "Thank you very much!")