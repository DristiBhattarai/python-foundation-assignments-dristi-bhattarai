"""
Exercise: Clean Numeric Values
Student: Dristi Bhattarai
Day: 2
"""
raw_values = [100, None, 250, "invalid", 300, None, 450]
clean_values = []

for value in raw_values:
    if not isinstance(value, int):
        continue
    clean_values.append(value)
print(clean_values)

#list_comprehension

raw_values = [100, None, 250, "invalid", 300, None, 450]
clean_values = [value for value in raw_values if isinstance(value, int)]
print(clean_values)