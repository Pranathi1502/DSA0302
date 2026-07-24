# ==========================================================
# Experiment 04
# Aim:
# Use the Porter Stemmer algorithm to perform
# word stemming on a list of words.
# ==========================================================

import nltk
from nltk.stem import PorterStemmer

# Download NLTK data (only the first time)
nltk.download('punkt')

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "playing",
    "running",
    "studies",
    "happiness",
    "jumped",
    "flying",
    "cats",
    "books",
    "easily",
    "connected"
]

print("========== PORTER STEMMER ==========\n")

for word in words:
    stem = stemmer.stem(word)
    print(f"Original Word : {word:12} Stemmed Word : {stem}")

print("\nWord Stemming Completed Successfully.")