# ChatGPT 🌟 Practice Problems - Boolean
# Mini-Challenge #2: Discount Calculator
# Rules
# If the total is over $100, they get 10% off
# If they are a member, they get 5% extra off
# If they are over 60, they get another 5% off
# Discounts stack, and are applied in order:
# Amount over $100 → 10% off
# If member → another 5% off
# If age > 60 → another 5% off
# total = 120.0
# member = "yes"
# age = 65
# answer = 97.47

total = float(input("What is the total amount spent? "))
member = input("Are you a rewards member? (yes/no) ")
age = int(input("What is your age? "))
final = total

if total > 100:
    final -= final * 0.10

if member.lower() == "yes":
    final -= final * 0.05

if age > 60:
    final -= (final * 0.05)

discount = total - final

print(f"Original total:\t${total:.2f}")
print(f"Discount applied:\t${discount:.2f}")
print(f"Final total:\t${final:.2f}")
