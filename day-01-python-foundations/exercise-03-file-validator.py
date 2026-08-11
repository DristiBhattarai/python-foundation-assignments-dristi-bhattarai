"""
Exercise: File Validator
Student: Dristi Bhattarai
Day: 1
"""
file_name = input("Enter a file name: ")
file_name = file_name.strip().lower()

if file_name.endswith(".csv"):
    print("File type: CSV")
elif file_name.endswith(".json"):
    print("File type: JSON")
elif file_name.endswith(".parquet"):
    print("File type: Parquet")
else:
    print("Unsupported file type")