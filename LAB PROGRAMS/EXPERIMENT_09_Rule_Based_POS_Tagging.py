# ==========================================================
# Experiment 09
# Aim:
# Rule-Based POS Tagging using Regular Expressions.
# ==========================================================

import nltk

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

tagger = nltk.RegexpTagger(patterns)

words = ["playing", "jumped", "books", "computer"]

print("Rule-Based POS Tagging\n")

for word in words:
    print(word, ":", tagger.tag([word])[0][1])

print("\nExperiment Completed Successfully.")