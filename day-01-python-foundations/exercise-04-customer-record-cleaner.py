"""
Exercise: Customer Record Cleaner
Student: Dristi Bhattarai
Day: 1
"""
raw_name = "sAgar THAPA"
raw_ciy = "kATHMANDU"
raw_age = "27"
raw_email = "SAGAR@MAIL.COM"

name = raw_name.strip().title()
city = raw_ciy.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

status = "Adult" if age >= 18 else "Minor"

print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")