# ==========================================================
# Inflectional Morphology-Based Normalization Module
# ==========================================================

words = ["create", "creates", "creating"]

print("{:<12}{:<10}{:<25}{:<12}{:<15}{:<15}".format(
    "Word", "Suffix", "Grammatical Category",
    "Root", "Normalized", "Final Output"))

print("-" * 95)

for word in words:

    root = "create"
    suffix = "-"
    category = "Base Form"

    if word.endswith("s") and word != "create":
        suffix = "s"
        category = "Third-Person Singular"

    elif word.endswith("ing"):
        suffix = "ing"
        category = "Present Participle"

    normalized = "create"

    print("{:<12}{:<10}{:<25}{:<12}{:<15}{:<15}".format(
        word, suffix, category, root, normalized, normalized))
