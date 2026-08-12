# Q4 - Morphological Error Analysis in Information Retrieval

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

# E-commerce search terms
words = [
    "watches",
    "watching",
    "washable",
    "washer",
    "washed"
]

print("MORPHOLOGICAL ERROR ANALYSIS")
print("---------------------------------------------")

print("\nWord\t\tPorter Stem\tType")
print("---------------------------------------------")

for word in words:

    stem = stemmer.stem(word)

    if word == "watches":
        suffix = "es"
        morph_type = "Inflectional"
    elif word == "watching":
        suffix = "ing"
        morph_type = "Inflectional"
    elif word == "washable":
        suffix = "able"
        morph_type = "Derivational"
    elif word == "washer":
        suffix = "er"
        morph_type = "Derivational"
    elif word == "washed":
        suffix = "ed"
        morph_type = "Inflectional"

    print(f"{word:<15}{stem:<15}{morph_type}")


# ---------------------------------------------
# Detailed error analysis
# ---------------------------------------------

print("\nDETAILED ERROR ANALYSIS")
print("---------------------------------------------")

analysis = {
    "watches": "watch + es -> Inflectional",
    "watching": "watch + ing -> Inflectional",
    "washable": "wash + able -> Derivational",
    "washer": "wash + er -> Derivational",
    "washed": "wash + ed -> Inflectional"
}

for word, explanation in analysis.items():
    print(word, ":", explanation)


# ---------------------------------------------
# Identify problematic derivational forms
# ---------------------------------------------

print("\nSTEMMING ERRORS")
print("---------------------------------------------")

for word in words:

    stem = stemmer.stem(word)

    if word in ["washable", "washer"]:
        print(word, "->", stem)
        print("ERROR: Derivational information may be lost.")

    else:
        print(word, "->", stem, "-> Inflectional form")


# ---------------------------------------------
# Improved preprocessing
# ---------------------------------------------

def improved_preprocess(word):

    # Preserve derivational forms
    derivational_words = ["washable", "washer"]

    if word in derivational_words:
        return word

    # Normalize only inflectional forms
    if word == "watches":
        return "watch"

    if word == "watching":
        return "watch"

    if word == "washed":
        return "wash"

    return word


print("\nIMPROVED PREPROCESSING")
print("---------------------------------------------")

for word in words:
    print(word, "->", improved_preprocess(word))


# ---------------------------------------------
# Conclusion
# ---------------------------------------------

print("\nCONCLUSION")
print("---------------------------------------------")
print("Inflectional suffixes such as -s, -ing and -ed")
print("can usually be normalized to their base forms.")

print("Derivational suffixes such as -able and -er")
print("should be preserved because they can change")
print("the meaning or grammatical category of a word.")

print("Therefore, morphological analysis is better")
print("than blindly applying Porter Stemmer to all words.")
