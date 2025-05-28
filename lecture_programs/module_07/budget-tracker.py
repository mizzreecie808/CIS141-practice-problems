# ChatGPT 💰 Budget Tracker App 💰
# Add expense (category, amount, date)
# View summary (total spent, by category, average expense)
# List all expenses, Delete expense, Exit program

expenses = []  # Global list to store expenses

def add_expense(expenses):
    print("Add a new expense (type 'quit' to stop adding).")

    while True:
        user_input = input("Enter expense name and amount (e.g., Coffee, 3.50): ")
        if user_input.lower().strip() == 'quit':
            print("✅ Finished adding expenses.\n")
            break

        parts = user_input.split(",")
        if len(parts) != 2:
            print("❌ Please enter in format: Name, Amount (e.g., Coffee, 3.50)")
            continue

        name = parts[0].strip().capitalize()
        try:
            amount = float(parts[1].strip())
        except ValueError:
            print("❌ Amount must be a number.")
            continue

        expenses.append({"name": name, "amount": amount})
        print(f"✅ Added expense: {name} - ${amount:.2f}")

def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses recorded yet.\n")
        return

    print("\n-- 🧾 Expense List 🧾 --")
    total = 0
    for expense in expenses:
        print(f"{expense['name']:<15} ${expense['amount']:>7.2f}")
        total += expense['amount']
    print(f"{'-'*25}\nTotal:          ${total:.2f}\n")

def main():
    print("Welcome to your Budget Tracker! 💵\n")

    while True:
        print("Choose an option:")
        print("1) Add Expense")
        print("2) View Expenses")
        print("3) Quit")

        choice = int(input("Enter choice (1/2/3): ").strip())

        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            print("👋 Goodbye! Thanks for using Budget Tracker.")
            break
        else:
            print("❌ Invalid choice, please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
