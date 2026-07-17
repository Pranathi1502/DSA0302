import re

reg = input("Enter Register Number: ").strip().upper()
email = input("Enter College Email: ").strip().lower()
course = input("Enter Course Code: ").strip().upper()
semester = input("Enter Semester (1-8): ").strip()
mobile = input("Enter Mobile Number: ").strip()

# Validation Patterns
reg_valid = re.fullmatch(r"\d{2}[A-Z]{3}\d{4}", reg)
email_valid = re.fullmatch(r"[a-z0-9._%+-]+@saveetha\.com", email)
course_valid = re.fullmatch(r"[A-Z]{3}\d{3}", course)
semester_valid = re.fullmatch(r"[1-8]", semester)
mobile_valid = re.fullmatch(r"[6-9]\d{9}", mobile)

print("\n------ Validation Results ------")

print("Register Number :", "Valid" if reg_valid else "Invalid")
print("College Email   :", "Valid" if email_valid else "Invalid")
print("Course Code     :", "Valid" if course_valid else "Invalid")
print("Semester        :", "Valid" if semester_valid else "Invalid")
print("Mobile Number   :", "Valid" if mobile_valid else "Invalid")

if reg_valid and email_valid and course_valid and semester_valid and mobile_valid:
    print("\nRegistration Status : Registration Successful")
else:
    print("\nRegistration Status : Registration Failed")
