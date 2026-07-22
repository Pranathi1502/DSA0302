# ==========================================================
# Experiment 02
# Aim:
# Demonstrate Morphological Analysis using the NLTK library.
# ==========================================================

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK data (only needed the first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# List of words
words = [
    "running",
    "studies",
    "playing",
    "better",
    "children",
    "cars",
    "wolves",
    "books"
]

print("========== MORPHOLOGICAL ANALYSIS ==========\n")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("Word       :", word)
    print("Stem       :", stem)
    print("Lemma      :", lemma)
    print("-" * 35)

print("\nMorphological Analysis Completed Successfully.")