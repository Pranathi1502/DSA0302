from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["analyzing", "analysis", "analytical"]

print("{:<15}{:<12}{:<12}{:<15}{:<15}".format(
    "Word", "Root", "Affix", "Type", "Normalized"))

print("-" * 75)

for word in words:

    if word.endswith("ing"):
        root = "analyze"
        affix = "ing"
        transformation = "Inflectional"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "sis"
        transformation = "Derivational"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "ical"
        transformation = "Derivational"

    else:
        root = ps.stem(word)
        affix = "-"
        transformation = "-"

    normalized = "analyze"

    print("{:<15}{:<12}{:<12}{:<15}{:<15}".format(
        word, root, affix, transformation, normalized))
