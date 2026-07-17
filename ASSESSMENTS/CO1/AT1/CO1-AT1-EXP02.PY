import re

products = [
    "Laptop",
    "Laptop Bag",
    "Mouse",
    "Wireless Mouse",
    "Keyboard",
    "Gaming Keyboard",
    "Smart Phone",
    "Phone Case"
]

keyword = input("Enter Search Keyword: ")

# Exact
exact = [p for p in products if re.fullmatch(keyword, p, re.I)]

# Prefix
prefix = [p for p in products if re.match(keyword, p, re.I)]

# Suffix
suffix = [p for p in products if re.search(keyword + r"$", p, re.I)]

# Partial
partial = [p for p in products if re.search(keyword, p, re.I)]

print("\nExact Match:", exact)
print("Prefix Match:", prefix)
print("Suffix Match:", suffix)
print("Partial Match:", partial)

print("\n------ Search Report ------")
print("Exact Matches :", len(exact))
print("Prefix Matches:", len(prefix))
print("Suffix Matches:", len(suffix))
print("Partial Matches:", len(partial))
