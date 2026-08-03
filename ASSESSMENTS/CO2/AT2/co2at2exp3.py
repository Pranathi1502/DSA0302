# ==========================================================
# Morphology-Based Normalization Module
# ==========================================================

words = ["govern", "government", "governance"]

print("{:<15}{:<10}{:<12}{:<20}{:<15}{:<15}".format(
    "Word", "Root", "Affix", "Derivational Level",
    "Normalized", "Final Output"))

print("-" * 95)

for word in words:

    root = "govern"
    affix = "-"
    level = "Base"

    if word.endswith("ment"):
        affix = "ment"
        level = "Level 1"

    elif word.endswith("ance"):
        affix = "ance"
        level = "Level 2"

    normalized = "govern"

    print("{:<15}{:<10}{:<12}{:<20}{:<15}{:<15}".format(
        word, root, affix, level, normalized, normalized))
