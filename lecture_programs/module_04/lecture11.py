# Problem #11: Campus Coffee Loyalty

cups = int(input("How many cups of coffee have you bought this month? "))
div_seven = cups % 7

if div_seven == 0 and cups >= 7:
    print("Free Drink")
else:
    print(f"You need {7 - div_seven} more for a discount")
