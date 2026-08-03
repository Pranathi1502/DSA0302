# ==========================================================
# Morphological Parsing using Rule-Based Decomposition
# ==========================================================

words = ["unhappy", "happiness", "happily"]

print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<12}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))

print("-" * 75)

for word in words:

    prefix = "-"
    suffix = "-"
    root = word
    transformation = "Base"

    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
        transformation = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        root = word[:-4]

        if root.endswith("i"):
            root = root[:-1] + "y"

        transformation = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        root = word[:-2]

        if root.endswith("i"):
            root = root[:-1] + "y"

        transformation = "Derivational"

    print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<12}".format(
        word, prefix, root, suffix, transformation, root))
