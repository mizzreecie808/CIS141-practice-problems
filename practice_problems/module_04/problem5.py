'''
Problem #5
A store charges $5 for shipping on any order under $50.
If the order amount is $50 or more, shipping is free.
Ask the user for the order total
Print the total cost, including shipping.
'''

order_amount = float(input("What is the order amount? "))

if order_amount > 50:
    print(f"Total cost is ${order_amount:.2f}, shipping is free.")
else:
    print(f"Total cost is ${order_amount + 5:.2f}, shipping costed $5.")
