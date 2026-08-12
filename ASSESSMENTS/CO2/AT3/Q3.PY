# Q3 - Error Analysis of Stemming in News Article Classification

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Words from news articles
words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organization's"
]

print("NEWS ARTICLE STEMMING ERROR ANALYSIS")
print("--------------------------------------")

print("\nWORD\t\tNO STEM\t\tPORTER STEM\tLEMMATIZATION")
print("-" * 65)

for word in words:

    # Remove possessive
    clean_word = word.replace("'s", "")

    # Porter Stemmer
    stem = stemmer.stem(clean_word)

    # Lemmatization
    lemma = lemmatizer.lemmatize(clean_word)

    print(f"{word:<15}{clean_word:<15}{stem:<15}{lemma}")


# -------------------------------------------------
# Identify incorrect Porter stems
# -------------------------------------------------

print("\nINCORRECT PORTER STEMS")
print("--------------------------------------")

for word in words:

    clean_word = word.replace("'s", "")
    stem = stemmer.stem(clean_word)

    print(word, "->", stem)

print("\nObservation:")
print("Porter Stemmer maps organization, organizer,")
print("organizing and organized to different forms.")
print("This can reduce semantic information during")
print("news classification.")


# -------------------------------------------------
# Feature Extraction Comparison
# -------------------------------------------------

print("\nFEATURE EXTRACTION")
print("--------------------------------------")

without_stemming = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organization"
]

porter_features = [
    stemmer.stem("organization"),
    stemmer.stem("organizer"),
    stemmer.stem("organizing"),
    stemmer.stem("organized"),
    stemmer.stem("organization")
]

lemma_features = [
    lemmatizer.lemmatize("organization"),
    lemmatizer.lemmatize("organizer"),
    lemmatizer.lemmatize("organizing", pos="v"),
    lemmatizer.lemmatize("organized", pos="v"),
    lemmatizer.lemmatize("organization")
]

print("Without Stemming :", without_stemming)
print("Porter Stemming  :", porter_features)
print("Lemmatization    :", lemma_features)


# -------------------------------------------------
# Final comparison
# -------------------------------------------------

print("\nPREPROCESSING COMPARISON")
print("--------------------------------------")

print("1. Without Stemming")
print("   Preserves maximum word information.")

print("\n2. Porter Stemming")
print("   Reduces words using suffix removal rules.")
print("   May produce unnatural stems.")

print("\n3. Lemmatization")
print("   Converts words to meaningful dictionary forms.")
print("   Usually preserves more semantic information.")

print("\nCONCLUSION")
print("--------------------------------------")
print("Lemmatization is preferred when semantic information")
print("is important for news article classification.")
