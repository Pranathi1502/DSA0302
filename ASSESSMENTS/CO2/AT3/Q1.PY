import re
from nltk.stem import PorterStemmer

# Create Porter Stemmer
stemmer = PorterStemmer()

# Biomedical words
text = """
Infection infectious infected infect
The infection was caused by an infectious agent.
The patient was infected with bacteria.
"""

# 1. Preprocessing
text = text.lower()
words = re.findall(r'\b[a-z]+\b', text)

print("PREPROCESSED WORDS")
print(words)

# 2. Apply Porter Stemmer
print("\nPORTER STEMMING RESULTS")
print("-" * 35)

for word in ["infection", "infectious", "infected", "infect"]:
    stem = stemmer.stem(word)
    print(f"{word:<12} -> {stem}")

# 3. Morphological analysis
print("\nMORPHOLOGICAL ANALYSIS")
print("-" * 45)

analysis = {
    "infection": "infect + ion  (derivational)",
    "infectious": "infect + ious (derivational)",
    "infected": "infect + ed   (inflectional)",
    "infect": "infect          (root)"
}

for word, meaning in analysis.items():
    print(f"{word:<12} : {meaning}")

# 4. Error identification
print("\nERROR ANALYSIS")
print("-" * 35)

for word in ["infection", "infectious", "infected", "infect"]:
    stem = stemmer.stem(word)

    if word == "infectious" and stem != "infect":
        print(f"ERROR: {word} -> {stem}")
        print("Derivational information is incorrectly removed.")
    else:
        print(f"{word} -> {stem} : Acceptable")

# 5. Final conclusion
print("\nCONCLUSION")
print("Porter Stemmer is useful for reducing inflectional forms.")
print("However, it may incorrectly remove derivational information.")
print("Therefore, inflectional and derivational morphology")
print("should be treated separately in biomedical NLP.")
