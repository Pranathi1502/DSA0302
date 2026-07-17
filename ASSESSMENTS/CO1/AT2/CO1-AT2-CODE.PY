# Morphology and Word Formation Demo

print("=== Morphology and Word Formation ===")

# Input word
word = input("Enter a word: ")

# Simple morphology examples
if word.lower() == "unhappiness":
    prefix = "un"
    root = "happy"
    suffix = "ness"

elif word.lower() == "replaying":
    prefix = "re"
    root = "play"
    suffix = "ing"

elif word.lower() == "careless":
    prefix = ""
    root = "care"
    suffix = "less"

elif word.lower() == "teacher":
    prefix = ""
    root = "teach"
    suffix = "er"

else:
    print("\nMorphological information not available for this word.")
    exit()

print("\n----- Morphological Analysis -----")
print("Word      :", word)
print("Prefix    :", prefix if prefix else "None")
print("Root Word :", root)
print("Suffix    :", suffix if suffix else "None")

print("\nWord Formation:")
if prefix:
    print(prefix, "+", root, "+", suffix, "=", word)
else:
    print(root, "+", suffix, "=", word)

print("\nMeaning:")
if prefix == "un":
    print("'un' means NOT")
elif prefix == "re":
    print("'re' means AGAIN")

print("\nMorphology Analysis Completed Successfully!")
