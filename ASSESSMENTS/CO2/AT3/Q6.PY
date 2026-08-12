# Q6 - Finite-State Morphological Parser
# Plural Noun Error Analysis

import nltk
from nltk.corpus import wordnet as wn

# Download WordNet once
try:
    wn.synsets("car")
except LookupError:
    nltk.download("wordnet")

# -----------------------------------------
# IRREGULAR PLURALS
# -----------------------------------------

irregular = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "feet": "foot",
    "teeth": "tooth",
    "geese": "goose",
    "people": "person",
    "oxen": "ox"
}

# -----------------------------------------
# CHECK WORD IN WORDNET
# -----------------------------------------

def is_noun(word):
    return len(wn.synsets(word, pos=wn.NOUN)) > 0


# -----------------------------------------
# PLURAL PARSER
# -----------------------------------------

def parser(word):

    word = word.lower()

    # 1. Check irregular plurals
    if word in irregular:
        return irregular[word], "Plural Noun - Irregular"

    # 2. Words ending in -ies
    # cities -> city
    if word.endswith("ies") and len(word) > 3:
        singular = word[:-3] + "y"

        if is_noun(singular):
            return singular, "Plural Noun - ies"

    # 3. Words ending in -es
    # boxes -> box
    if word.endswith("es") and len(word) > 2:

        singular = word[:-2]

        if is_noun(singular):
            return singular, "Plural Noun - es"

    # 4. Regular plural ending in -s
    # cars -> car
    if word.endswith("s") and len(word) > 1:

        singular = word[:-1]

        if is_noun(singular):
            return singular, "Plural Noun - s"

    # 5. If no plural rule matches
    return word, "Singular / Not recognized"


# -----------------------------------------
# TEST WORDS
# -----------------------------------------

words = [
    "cars",
    "boxes",
    "cities",
    "children",
    "dogs",
    "books",
    "watches",
    "buses",
    "men",
    "women",
    "mice",
    "people",
    "cat"
]

print("FINITE-STATE MORPHOLOGICAL PARSER")
print("=" * 55)

print("{:<15} {:<15} {}".format(
    "WORD", "ROOT", "ANALYSIS"
))

print("-" * 55)

for w in words:

    root, analysis = parser(w)

    print("{:<15} {:<15} {}".format(
        w, root, analysis
    ))


# -----------------------------------------
# ERROR ANALYSIS
# -----------------------------------------

print("\nERROR ANALYSIS")
print("=" * 55)

print("Original parser:")
print("word[:-2] was used for every word ending in 's'.")

print("\nExamples of original errors:")
print("cars     -> ca")
print("boxes    -> box")
print("cities   -> cit")
print("children -> children")

print("\nCorrected parser:")
print("cars     -> car")
print("boxes    -> box")
print("cities   -> city")
print("children -> child")

print("\nLIMITATION:")
print("Rule-based parsing cannot handle every English")
print("plural because English contains many irregular forms.")
