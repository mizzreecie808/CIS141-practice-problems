# Chat 🧪 No-Input Dictionary Practice Problems
# 2. Top Seller Analyzer 🎯
# Calculate total sales for each item
# Identify best selling item
# Track any item with average below 5
# Sort items by total sales (high to low)
# Print report

sales_data = {
    "notebook": [5, 7, 6, 4],
    "pen": [10, 12, 11, 14],
    "eraser": [1, 0, 3, 2],
    "marker": [4, 4, 5, 6]
}

def top_sales(sales):
    best_seller = ("", 0)
    for item, qty_list in sales.items():
        total = sum(qty_list)
        if total > best_seller[1]:
            best_seller = (item, total)

    print(f"🏆 Best Seller: {best_seller[0]} with {best_seller[1]} units sold")
    return best_seller

def sales_per_item(sales):
    totals = {}
    average_sales = {}
    for item, qty_list in sales.items():
        totals[item] = sum(qty_list)
        average_sales[item] = round(sum(qty_list) / len(qty_list), 2)

    print("📊 Total Sales Per Item:")
    print(totals)
    print("📊 Average Sales Per Item:")
    print(average_sales)
    return totals, average_sales

sales_per_item(sales_data)
top_sales(sales_data)
