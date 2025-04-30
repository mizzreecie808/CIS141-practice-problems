'''
Problem #3
Prompt the user for their bank balance.
Evaluate whether the balance is less than $100.
Print True if the user’s balance is below $100;
Print False, otherwise.
'''

balance = float(input("What is your bank balance? "))
if balance < 100:
    print(True)
else:
    print(False)
