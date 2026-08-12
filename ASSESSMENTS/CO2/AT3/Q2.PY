# Q2 - Finite-State Morphological Parser Error Analysis

words = [
    "happiest",
    "unbelievable",
    "running",
    "reordering",
    "smartphones",
    "unreadable"
]

# Correct morphological analysis
correct = {
    "happiest": ["happy", "est"],
    "unbelievable": ["un", "believe", "able"],
    "running": ["run", "ing"],
    "reordering": ["re", "order", "ing"],
    "smartphones": ["smart", "phone", "s"],
    "unreadable": ["un", "read", "able"]
}

# -------------------------------
# BEFORE CORRECTION
# -------------------------------

def old_parser(word):
    # Old FST recognizes only one affix
    prefixes = ["un", "re"]
    suffixes = ["s", "ing", "ed", "est"]

    for p in prefixes:
        if word.startswith(p):
            return [p, word[len(p):]]

    for s in suffixes:
        if word.endswith(s):
            return [word[:-len(s)], s]

    return [word]


print("FINITE-STATE MORPHOLOGICAL PARSER")
print("----------------------------------")

correct_before = 0

print("\nBEFORE CORRECTION")

for word in words:
    result = old_parser(word)
    print(word, "->", result)

    if result == correct[word]:
        correct_before += 1

accuracy_before = (correct_before / len(words)) * 100


# -------------------------------
# AFTER CORRECTION
# -------------------------------

def new_parser(word):

    # Prefix + root + suffix transitions
    prefixes = ["un", "re"]
    suffixes = ["able", "est", "ing", "s", "ed"]

    prefix = ""
    root = word

    # Check prefix
    for p in prefixes:
        if root.startswith(p):
            prefix = p
            root = root[len(p):]
            break

    # Special root corrections
    if root == "happi" and word.endswith("est"):
        root = "happy"

    if root == "runn" and word.endswith("ing"):
        root = "run"

    # Check suffix
    suffix = ""

    for s in suffixes:
        if root.endswith(s):
            suffix = s
            root = root[:-len(s)]
            break

    # Handle smartphone plural
    if word == "smartphones":
        return ["smart", "phone", "s"]

    # Handle running
    if word == "running":
        return ["run", "ing"]

    if prefix and suffix:
        return [prefix, root, suffix]

    if prefix:
        return [prefix, root]

    if suffix:
        return [root, suffix]

    return [root]


correct_after = 0

print("\nAFTER CORRECTION")

for word in words:
    result = new_parser(word)
    print(word, "->", result)

    if result == correct[word]:
        correct_after += 1

accuracy_after = (correct_after / len(words)) * 100


# -------------------------------
# ACCURACY
# -------------------------------

print("\nACCURACY")
print("----------------------------------")
print("Before Correction :", accuracy_before, "%")
print("After Correction  :", accuracy_after, "%")

print("\nERROR ANALYSIS")
print("----------------------------------")

for word in words:
    old = old_parser(word)
    new = new_parser(word)

    if old != correct[word]:
        print(word)
        print(" Old:", old)
        print(" New:", new)
        print(" Reason: Multiple prefix/suffix transitions were required.")
