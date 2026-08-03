# ==========================================================
# Finite-State Morphological Parser
# ==========================================================

words = ["writes", "writing", "written"]

print("{:<12}{:<35}{:<12}{:<12}{:<15}{:<12}".format(
    "Word", "State Transition", "Root", "Suffix", "Pattern", "Normalized"))

print("-" * 100)

for word in words:

    if word == "writes":
        path = "q0 → q1 → q2"
        root = "write"
        suffix = "s"
        pattern = "Regular"
        normalized = "write"

    elif word == "writing":
        path = "q0 → q1 → q3"
        root = "write"
        suffix = "ing"
        pattern = "Regular"
        normalized = "write"

    elif word == "written":
        path = "q0 → q4"
        root = "write"
        suffix = "en"
        pattern = "Irregular"
        normalized = "write"

    print("{:<12}{:<35}{:<12}{:<12}{:<15}{:<12}".format(
        word, path, root, suffix, pattern, normalized))
