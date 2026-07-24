# ==========================================================
# Experiment 10
# Aim: Transformation-Based POS Tagging.
# ==========================================================

words = [
    ("running", "NN"),
    ("cats", "NN"),
    ("played", "NN"),
    ("book", "NN")
]

print("Before Transformation:\n")

for word, tag in words:
    print(word, ":", tag)

print("\nAfter Transformation:\n")

for word, tag in words:

    if word.endswith("ing"):
        tag = "VBG"

    elif word.endswith("ed"):
        tag = "VBD"

    elif word.endswith("s"):
        tag = "NNS"

    print(word, ":", tag)

print("\nTransformation-Based Tagging Completed Successfully.")