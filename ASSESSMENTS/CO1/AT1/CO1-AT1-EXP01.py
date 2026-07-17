import re

resume = """
Name: Pranathi Chowdary
Email: pranathi123@gmail.com
Mobile: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Name
name = re.search(r"Name:\s*([A-Za-z ]+)", resume)
name = name.group(1)

# Email
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Mobile
mobile = re.findall(r"\b[6-9]\d{9}\b", resume)

# Skills
skill_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
skills = [s for s in skill_list if re.search(s, resume, re.I)]

# Experience
exp = re.search(r"(\d+)\s*years?", resume)
experience = int(exp.group(1))

# Summary
print("------ Candidate Profile ------")
print("Name:", name)
print("Email:", email[0])
print("Mobile:", mobile[0])
print("Skills:", ", ".join(skills))
print("Experience:", experience, "Years")

# Eligibility
if experience >= 2 and "Python" in skills:
    print("Status: Eligible for Shortlisting")
else:
    print("Status: Not Eligible")
