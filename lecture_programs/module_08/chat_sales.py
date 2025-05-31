# Chat 🧪 No-Input Dictionary Practice Problems
# 2. Top Seller Analyzer 🎯
# Calculate total sales for each item
# Identify best selling item
# Track any item with average below 5
# Sort items by total sales (high to low)
# Print report
from datetime import datetime

sales_data = {
    "notebook": [5, 7, 6, 4],
    "pen": [10, 12, 11, 14],
    "eraser": [1, 0, 3, 2],
    "marker": [4, 4, 5, 6]
}

# ✅ Calculates and prints total sales for each item
def sales_per_item(sales):
    totals = {}
    for item, qty_list in sales.items():
        totals[item] = sum(qty_list)

    print(f"{'📊 Total Sales Per Item':^40}")
    sorted_dict = dict(sorted(totals.items(), key=lambda item: item[1]))
    print_items(sorted_dict)
    return totals

# ✅ Calculates and prints total sales for each item
def average_sales(sales):
    average = {}
    for item, qty_list in sales.items():
        average[item] = round(sum(qty_list) / len(qty_list), 2)

    print(f"{'📊 Average Sales Per Item':^40}")
    sorted_dict = dict(sorted(average.items(), key=lambda item: item[1]))
    print_items(sorted_dict)
    return average

# 🏆 Identifies and prints the best-selling item
def top_sales(sales):
    best_seller = ("", 0)
    for item, qty_list in sales.items():
        total = sum(qty_list)
        if total > best_seller[1]:
            best_seller = (item, total)

    print(f"🏅 Best Seller: {best_seller[0]} with {best_seller[1]} units sold")
    return best_seller

# 📋 Helper function to print lines with the same formatting
def print_items(dict):
    for key, val in dict.items():
        print(f"{f'{key}:':<12} {val:>6} units")

# 💾 Writes the sales report to a text file
def export_report(totals, averages, best_seller, filename="sales_report.txt"):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as file:
        file.write(f"Sales Report Generated: {timestamp}\n")
        file.write("=" * 40 + "\n")

        file.write("Total Sales Per Item:\n")
        for item, total in totals.items():
            file.write(f"{item:<12} {total:>6} units\n")

        file.write("\nAverage Sales Per Item:\n")
        for item, avg in averages.items():
            file.write(f"{item:<12} {avg:>6} units\n")

        file.write("\nBest Seller:\n")
        file.write(f"{best_seller[0]} with {best_seller[1]} units sold\n")

    print(f"\n✅ Report exported to: {filename}")

# 🧭 Main function to organize logic
def main():
    print(f"{'📦 Running Sales Analyzer...':^40}")
    print("-"*40)
    totals = sales_per_item(sales_data)
    print("-"*40)
    averages = average_sales(sales_data)
    print("-"*40)
    best_seller = top_sales(sales_data)
    print("-"*40)
    export_report(totals, averages, best_seller)

# 🚀 Start here only if file is run directly
if __name__ == "__main__":
    main()
