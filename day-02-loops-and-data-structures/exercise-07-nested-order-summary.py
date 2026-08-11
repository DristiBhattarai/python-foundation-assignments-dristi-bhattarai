"""
Exercise: Nested Order Summary
Student: Dristi Bhattarai
Day: 2
"""
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer.
for order_id, order in orders.items():
    print(order_id, "-", order["customer"])

# 2. Print only completed orders.
print("\nCompleted orders:")

for order_id, order in orders.items():
    if order["status"] == "Completed":
        print(order_id, "-", order["customer"])

# 3. Calculate the total amount of completed orders.
total_completed = sum(
    order["amount"]
    for order in orders.values()
    if order["status"] == "Completed"
)

# 4. Count pending orders.
pending_count = sum(
    1
    for order in orders.values()
    if order["status"] == "Pending"
)

# 5. Add a new order.
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 2100,
    "status": "Pending"
}

print("\nTotal completed amount:", total_completed)
print("Pending orders:", pending_count)
print("Updated orders:", orders)