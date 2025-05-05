# Problem #9: Textbook Bulk Discount

books_purchased = int(input("How many books did you purchase? "))
pre_discount = books_purchased * 99.99

if books_purchased < 3:
    pre_discount = pre_discount
elif 3 <= books_purchased <= 5:
    pre_discount -= pre_discount * 0.05
elif 6 <= books_purchased <= 9:
    pre_discount -= pre_discount * 0.1
else:
    pre_discount -= pre_discount * 0.15

print(f"Total cost: ${pre_discount:.2f}")
