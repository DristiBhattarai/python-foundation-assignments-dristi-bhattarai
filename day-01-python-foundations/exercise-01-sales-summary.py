"""
Exercise: Sales Summary
Student: Dristi Bhattarai
Day: 1
"""
# Input values
product_name = "Wireless Mouse"
unit_price = 1500
quality_sold = 12
discount_percentage = 0.10

# Calculation
gross_sales = unit_price * quality_sold
discount_amount = gross_sales * discount_percentage
final_sales = gross_sales - discount_amount

# Output
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales:.2f}")
