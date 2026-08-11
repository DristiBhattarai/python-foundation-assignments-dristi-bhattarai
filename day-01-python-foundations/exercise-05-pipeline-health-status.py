"""
Exercise: Pipeline Health Status
Student: Dristi Bhattarai
Day: 1
"""
# Test 1
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

total_rows = rows_loaded + rows_failed
failure_rate = (rows_failed / total_rows) * 100

if failure_rate <=2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"
    
print(f"Failure rate: {failure_rate:.2f}%")
print(f"Pipeline status: {status}")

# Test 2
rows_loaded = 9500
rows_failed = 500
runtime_minutes = 15

total_rows = rows_loaded + rows_failed
failure_rate = (rows_failed / total_rows) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

print(f"Failure rate: {failure_rate:.2f}%")
print(f"Pipeline status: {status}")
print()

# Test 3
rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

total_rows = rows_loaded + rows_failed
failure_rate = (rows_failed / total_rows) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

print(f"Failure rate: {failure_rate:.2f}%")
print(f"Pipeline status: {status}")

# The failure rate is low, but the runtime is high. Therefore, it should not be classified as Healthy.