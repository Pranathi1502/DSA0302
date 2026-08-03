from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("{:<12}{:<20}{:<20}{:<12}".format(
    "Word", "Applied Rule", "Final Stem", "Normalized"))

print("-" * 70)

for word in words:

    if word.endswith("ational"):
        rule = "Remove 'ational'"

    elif word.endswith("ation"):
        rule = "Remove 'ation'"

    elif word.endswith("ate"):
        rule = "Remove 'ate'"

    else:
        rule = "Porter Stemmer"

    stem = ps.stem(word)

    print("{:<12}{:<20}{:<20}{:<12}".format(
        word, rule, stem, stem))
