# ChatGPT 🧾 Mini App 3: Sales Tax Calculator
# 🧮 LEVEL 2: Intermediate Calculations - Apply Discount
# User enter multiple item prices
# Calculate subtotal
# Ask for sales tax rate
# Calculate tax amount
# Output subtotal, tax and total

print("🔹 Sales Tax Calculator 🔹")
print("  To calculate, type 'q'")
print("━" * 30)

prices = []

while True:
    user_input = input(f"{'Amount:':<15} ${'':>5}").strip().lower()

    if user_input == "q":
        if not prices:
            print("🛑 No amounts entered. Nothing to calculate.")
            break

        try:
            tax_rate = float(input("Sales tax rate (%): ").strip())
            discount_rate = float(input("Discount rate (%): ").strip())

            if tax_rate < 0 or discount_rate < 0:
                print("⚠️ Please enter a positive tax rate.")
                continue
        except ValueError:
            print("❌ Invalid rate. Please enter a number.")
            continue

        subtotal = sum(prices)
        discount = subtotal * (discount_rate / 100)
        tax = (subtotal - discount) * (tax_rate / 100)
        total = (subtotal - discount) + tax

        print("\n🧾 Summary")
        print("━" * 30)
        # Left-align the label in a 15-character space
        # Right-align the amount in 10 spaces, 2 decimal places
        # Show in sorted order
        for i, p in enumerate(sorted(prices), 1):
            print(f"  {i:>12}. ${p:>10.2f}")
        print("━" * 30)
        print(f"{'Subtotal:':<15} ${subtotal:>10.2f}")
        print(f"{'Discount Taken:':<15} ${discount:>10.2f}")
        print(f"{'Sales Tax:':<15} ${tax:>10.2f}")
        print(f"{'Total:':<15} ${total:>10.2f}")
        print("━" * 30)
        break

    try:
        value = float(user_input)
        if value < 0:
            print("⚠️ Please enter a positive number.")
        # run code here, input has been validated
        else:
            prices.append(value)

    except ValueError:
        print("❌ Invalid input. Please enter a number (e.g., 12 or 12.99).")

