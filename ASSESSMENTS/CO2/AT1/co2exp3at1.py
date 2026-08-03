from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["played", "player", "playing"]

print("{:<12}{:<10}{:<15}{:<15}{:<12}".format(
    "Word", "Stem", "Removed Affix", "Type", "Normalized"))

print("-" * 70)

for word in words:

    affix = "-"
    transformation = "Base"

    if word.endswith("ed"):
        affix = "ed"
        transformation = "Inflectional"

    elif word.endswith("ing"):
        affix = "ing"
        transformation = "Inflectional"

    elif word.endswith("er"):
        affix = "er"
        transformation = "Derivational"

    stem = ps.stem(word)

    print("{:<12}{:<10}{:<15}{:<15}{:<12}".format(
        word, stem, affix, transformation, stem))
