"""
Exercise: Dataset Comparison
Student: Dristi Bhattarai
Day: 2
"""
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# All unique dataset names
all_datasets = dataset_a | dataset_b

# Datasets found in both groups
both_groups = dataset_a & dataset_b

# Datasets only in dataset_a
only_a = dataset_a - dataset_b

# Datasets only in dataset_b
only_b = dataset_b - dataset_a

print("All unique datasets:", all_datasets)
print("Datasets in both groups:", both_groups)
print("Only in dataset_a:", only_a)
print("Only in dataset_b:", only_b)