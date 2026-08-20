import re

expression = input("Enter a logical expression: ").strip()

pattern = r'^(∀|∃)?[a-zA-Z][a-zA-Z0-9_]*\s*\(\s*[A-Za-z][A-Za-z0-9_]*\s*\(\s*[a-zA-Z0-9]+\s*\)\s*(→|∧|∨)\s*[A-Za-z][A-Za-z0-9_]*\s*\(\s*[a-zA-Z0-9]+\s*\)\s*\)$'

print("\nFOPC Parsing Result:")

if re.match(pattern, expression):
    print("Valid FOPC expression")
else:
    print("Invalid FOPC expression")