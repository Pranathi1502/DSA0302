# ==========================================================
# Experiment 03
# Aim:
# Implement a Finite-State Machine for Morphological Parsing
# to generate plural forms of English nouns.
# ==========================================================

# Function to generate plural forms
def generate_plural(noun):

    if noun.endswith("y"):
        return noun[:-1] + "ies"

    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    else:
        return noun + "s"


# List of nouns
nouns = [
    "cat",
    "dog",
    "bus",
    "box",
    "baby",
    "church",
    "class",
    "fox"
]

print("========== MORPHOLOGICAL PARSING ==========\n")

for noun in nouns:
    plural = generate_plural(noun)
    print(f"Singular : {noun:10}  Plural : {plural}")

print("\nPlural Generation Completed Successfully.")