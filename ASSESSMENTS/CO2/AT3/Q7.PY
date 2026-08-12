# QUESTION 7
# Error Analysis of Morphological Feature Extraction

import time
import re

from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -------------------------------------------------
# CREATE PORTER STEMMER
# -------------------------------------------------

stemmer = PorterStemmer()


# -------------------------------------------------
# SAMPLE NEWS DOCUMENTS
# -------------------------------------------------

documents = [
    "The company is organizing new business projects.",
    "The organization organized several business events.",
    "Workers are working on new technology development.",
    "The technology company is developing new software.",
    "Students are studying computer science studies.",
    "The students studied artificial intelligence.",
    "The football players are playing a match.",
    "The players played very well in the game.",
    "The government announced new economic policies.",
    "The governments are developing new policies.",
    "The company is connecting computers.",
    "The engineers connected the network.",
    "The researchers are researching new technology.",
    "The research organization developed software.",
    "Businesses are growing rapidly in the market.",
    "The business growth increased this year.",
    "The sports team is training new players.",
    "The trained players are preparing for matches.",
    "Technology organizations are developing applications.",
    "The developers developed a new application."
]

labels = [
    "business",
    "business",
    "technology",
    "technology",
    "technology",
    "technology",
    "sport",
    "sport",
    "business",
    "business",
    "technology",
    "technology",
    "technology",
    "technology",
    "business",
    "business",
    "sport",
    "sport",
    "technology",
    "technology"
]


# -------------------------------------------------
# STEMMING FUNCTION
# -------------------------------------------------

def stem_document(text):

    words = re.findall(r"[a-zA-Z]+", text.lower())

    stems = []

    for word in words:
        stems.append(stemmer.stem(word))

    return " ".join(stems)


# -------------------------------------------------
# ORIGINAL PIPELINE
# -------------------------------------------------

print("=" * 60)
print("ORIGINAL PIPELINE")
print("=" * 60)

start = time.time()

vectorizer_original = CountVectorizer()

X_original = vectorizer_original.fit_transform(documents)

original_vocabulary = vectorizer_original.get_feature_names_out()

# Stemming AFTER feature extraction
stemmed_features = [
    stemmer.stem(word)
    for word in original_vocabulary
]

original_time = time.time() - start

print("\nOriginal Vocabulary:")
print(list(original_vocabulary))

print("\nStemmed Features:")
print(stemmed_features)

print("\nVocabulary Size Before Correction:",
      len(original_vocabulary))


# -------------------------------------------------
# CORRECTED PIPELINE
# -------------------------------------------------

print("\n")
print("=" * 60)
print("CORRECTED PIPELINE")
print("=" * 60)

start = time.time()

# Stem BEFORE CountVectorizer

stemmed_documents = []

for document in documents:
    stemmed_documents.append(
        stem_document(document)
    )

vectorizer_correct = CountVectorizer()

X_correct = vectorizer_correct.fit_transform(
    stemmed_documents
)

correct_vocabulary = vectorizer_correct.get_feature_names_out()

correct_time = time.time() - start

print("\nStemmed Documents:")

for document in stemmed_documents[:5]:
    print(document)

print("\nCorrected Vocabulary:")
print(list(correct_vocabulary))

print("\nVocabulary Size After Correction:",
      len(correct_vocabulary))


# -------------------------------------------------
# CLASSIFICATION
# -------------------------------------------------

print("\n")
print("=" * 60)
print("CLASSIFICATION")
print("=" * 60)

# Split original data
X_train, X_test, y_train, y_test = train_test_split(
    documents,
    labels,
    test_size=0.3,
    random_state=42,
    stratify=labels
)


# -------------------------------------------------
# CLASSIFIER WITHOUT STEMMING
# -------------------------------------------------

vectorizer1 = CountVectorizer()

X_train1 = vectorizer1.fit_transform(X_train)
X_test1 = vectorizer1.transform(X_test)

model1 = LogisticRegression(
    max_iter=1000
)

model1.fit(X_train1, y_train)

prediction1 = model1.predict(X_test1)

accuracy1 = accuracy_score(
    y_test,
    prediction1
)


# -------------------------------------------------
# CLASSIFIER WITH STEMMING
# -------------------------------------------------

train_stemmed = [
    stem_document(text)
    for text in X_train
]

test_stemmed = [
    stem_document(text)
    for text in X_test
]

vectorizer2 = CountVectorizer()

X_train2 = vectorizer2.fit_transform(train_stemmed)
X_test2 = vectorizer2.transform(test_stemmed)

model2 = LogisticRegression(
    max_iter=1000
)

model2.fit(X_train2, y_train)

prediction2 = model2.predict(X_test2)

accuracy2 = accuracy_score(
    y_test,
    prediction2
)


# -------------------------------------------------
# FINAL COMPARISON
# -------------------------------------------------

print("\n")
print("=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print("\nWithout Stemming")
print("------------------------")
print("Vocabulary Size :", len(
    vectorizer1.get_feature_names_out()
))
print("Accuracy        :", round(
    accuracy1 * 100, 2
), "%")

print("\nWith Correct Stemming")
print("------------------------")
print("Vocabulary Size :", len(
    vectorizer2.get_feature_names_out()
))
print("Accuracy        :", round(
    accuracy2 * 100, 2
), "%")

print("\nProcessing Time")
print("------------------------")
print("Original Pipeline :", round(
    original_time, 4
), "seconds")

print("Corrected Pipeline:", round(
    correct_time, 4
), "seconds")


# -------------------------------------------------
# ERROR ANALYSIS
# -------------------------------------------------

print("\n")
print("=" * 60)
print("ERROR ANALYSIS")
print("=" * 60)

test_words = [
    "running",
    "runners",
    "runs",
    "studies",
    "studied",
    "studying",
    "organization",
    "organized",
    "organizer"
]

print("\nWORD              STEM")
print("-" * 35)

for word in test_words:
    print(
        "{:<18}{}".format(
            word,
            stemmer.stem(word)
        )
    )


# -------------------------------------------------
# CONCLUSION
# -------------------------------------------------

print("\n")
print("=" * 60)
print("CONCLUSION")
print("=" * 60)

print("1. The original program performs stemming")
print("   AFTER feature extraction.")

print("2. This creates redundant vocabulary.")

print("3. The corrected program performs stemming")
print("   BEFORE CountVectorizer.")

print("4. This reduces redundant morphological features.")

print("5. A smaller vocabulary can reduce memory usage")
print("   and improve NLP processing efficiency.")
