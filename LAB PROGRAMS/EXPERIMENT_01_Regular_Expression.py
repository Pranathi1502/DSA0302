# ==========================================================
# Experiment 01
# Aim:
# Demonstrate how to use Regular Expressions in Python
# to match and search for patterns in text.
# ==========================================================

import re

# Sample text
text = """
Name: Pranathi Chowdary
Email: pranathi1502@gmail.com
Phone: 9876543210
Department: CSE
Skills: Python, Java, SQL, Machine Learning
"""

print("========== ORIGINAL TEXT ==========")
print(text)

# Search for Name
name = re.search(r"Name:\s(.+)", text)
if name:
    print("Name:", name.group(1))

# Search for Email
email = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
if email:
    print("Email:", email.group())

# Search for Phone Number
phone = re.search(r"\d{10}", text)
if phone:
    print("Phone Number:", phone.group())

# Search for Department
department = re.search(r"Department:\s(\w+)", text)
if department:
    print("Department:", department.group(1))

# Find all Skills
skills = re.findall(r"Python|Java|SQL|Machine Learning", text)
print("Skills:", skills)

print("\nRegular Expression Matching and Searching Completed Successfully.")