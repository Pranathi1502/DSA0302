# ==========================================================
# Morphological Parser using Rule-Based Analysis
# ==========================================================

words = ["disagree", "agreement", "agreeable"]

print("{:<15}{:<10}{:<10}{:<10}{:<15}{:<25}{:<12}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Semantic Meaning", "Normalized"))

print("-" * 110)

for word in words:

    prefix = "-"
    suffix = "-"
    root = "agree"
    transformation = "Base"
    meaning = "Agreement"

    if word.startswith("dis"):
        prefix = "dis"
        transformation = "Derivational"
        meaning = "Negative agreement"

    elif word.endswith("ment"):
        suffix = "ment"
        transformation = "Derivational"
        meaning = "State of agreement"

    elif word.endswith("able"):
        suffix = "able"
        transformation = "Derivational"
        meaning = "Capable of agreement"

    normalized = "agree"

    print("{:<15}{:<10}{:<10}{:<10}{:<15}{:<25}{:<12}".format(
        word, prefix, root, suffix, transformation, meaning, normalized))
