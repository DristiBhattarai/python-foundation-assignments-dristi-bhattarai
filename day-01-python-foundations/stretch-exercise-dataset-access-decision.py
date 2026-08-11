"""
Exercise: Dataset Access Decision
Student: Dristi Bhattarai
Day: 1
"""
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]

# Access Granted
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print("Access granted.")
    
# User is inactive
user_role = "analyst"
is_active = False
requested_dataset = "sales_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print("Access granted.")
    
# Role is not allowed
user_role = "manager"
is_active = True
requested_dataset = "sales_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print("Access granted.")
    
# Dataset is restricted
user_role = "scientist"
is_active = True
requested_dataset = "salary_data"

if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print("Access granted.")