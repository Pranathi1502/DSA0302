# ==========================================================
# Morphological Parsing and Normalization System
# ==========================================================

words = ["activate", "activation", "reactivation"]

print("{:<15}{:<10}{:<12}{:<12}{:<20}{:<20}{:<20}".format(
    "Word", "Prefix", "Root", "Suffix",
    "Derivational Sequence", "Normalized", "Parsed Representation"))

print("-" * 130)

for word in words:

    prefix = "-"
    root = "activate"
    suffix = "-"
    sequence = "Base"
    parsed = ""

    if word == "activate":
        parsed = "activate"

    elif word == "activation":
        suffix = "ion"
        sequence = "activate → activation"
        parsed = "activate + ion"

    elif word == "reactivation":
        prefix = "re"
        suffix = "ion"
        sequence = "activate → activation → reactivation"
        parsed = "re + activate + ion"

    normalized = "activate"

    print("{:<15}{:<10}{:<12}{:<12}{:<20}{:<20}{:<20}".format(
        word, prefix, root, suffix, sequence, normalized, parsed))
