"""
Exercise: Sales List Analysis
Student: Dristi Bhattarai
Day: 2
"""
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Sorted from highest to lowest.
sorted_sales = sorted(monthly_sales, reverse=True)

# 2. A list containing only values above 100000.
above_ten_thousand = [amount for amount in monthly_sales if amount > 100000]

# 3. A list where each amount has 13% tax added.
sales_with_tax = [amount * 1.13 for amount in monthly_sales]

# 4. The total sales amount.
total_sales = sum(monthly_sales)

# 5. The average sales amount.
average_sales = total_sales / len(monthly_sales)

print("Sorted sales:", sorted_sales)
print("Above 10000:", above_ten_thousand)
print("Sales with 13% tax:", sales_with_tax)
print("Total sales:", total_sales)
print("Average sales:", average_sales)
