# ==========================================================
# Experiment 10
# Aim:
# Implement Transformation-Based POS Tagging.
# ==========================================================

words = [
    ("running", "NN"),
    ("played", "NN"),
    ("cats", "NN"),
    ("book", "NN")
]

print("Before Transformation\n")

for word, tag in words:
    print(word, ":", tag)

print("\nAfter Transformation\n")

for word, tag in words:

    if word.endswith("ing"):
        tag = "VBG"

    elif word.endswith("ed"):
        tag = "VBD"

    elif word.endswith("s"):
        tag = "NNS"

    print(word, ":", tag)

print("\nExperiment Completed Successfully.")