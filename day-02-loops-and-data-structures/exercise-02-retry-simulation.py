"""
Exercise: Retry Simulation
Student: Dristi Bhattarai
Day: 2
"""
attempt = 1
max_attempts = 3
operaion_successful = False

while attempt <= max_attempts:
    print(f"Attempt {attempt}")
    
    if attempt == 2:
        operation_successful = True
        break
    attempt += 1
    
if operaion_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")
    