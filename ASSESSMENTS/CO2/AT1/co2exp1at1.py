from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["connected", "connecting", "connection"]

print("{:<12}{:<10}{:<12}{:<15}{:<12}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))

print("-" * 65)

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        t = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        t = "Inflectional"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        t = "Derivational"

    else:
        root = word
        suffix = "-"
        t = "-"

    normalized = ps.stem(word)

    print("{:<12}{:<10}{:<12}{:<15}{:<12}".format(
        word, root, suffix, t, normalized))
