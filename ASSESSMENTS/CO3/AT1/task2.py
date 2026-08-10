import re
from collections import Counter

# --------------------------------
# Training Corpus
# --------------------------------

corpus = """
The student is studying natural language processing.
The student is learning Python programming.
The student is reading a book.
The student is writing an assignment.
The student is solving problems.
The student is practicing Python programming.
The teacher is teaching natural language processing.
The teacher is explaining the topic.
The teacher gives the student a book.
The teacher is helping students.
The student learns machine learning.
The student studies machine learning.
Students are learning Python.
Students are reading books.
Natural language processing is interesting.
Python programming is interesting.
Machine learning is useful.
The book is useful for students.
The student is using Python.
The student is learning machine learning.
"""

# --------------------------------
# Preprocessing
# --------------------------------

corpus = corpus.lower()

sentences = corpus.split(".")

tokens = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)
    tokens.extend(words)

# --------------------------------
# N-gram Frequency
# --------------------------------

unigram = Counter(tokens)

bigram = Counter()
trigram = Counter()

for i in range(len(tokens) - 1):
    bigram[(tokens[i], tokens[i + 1])] += 1

for i in range(len(tokens) - 2):
    trigram[(tokens[i], tokens[i + 1], tokens[i + 2])] += 1


# --------------------------------
# Probability Functions
# --------------------------------

def unigram_probability(word):
    return unigram[word] / len(tokens)


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# --------------------------------
# Unsmoothed Prediction
# --------------------------------

def unsmoothed_prediction(w1, w2, word):

    return trigram_probability(w1, w2, word)


# --------------------------------
# Backoff Prediction
# --------------------------------

def backoff_probability(w1, w2, word):

    # Try trigram first
    if trigram[(w1, w2, word)] > 0:

        return trigram_probability(w1, w2, word)

    # Backoff to bigram
    elif bigram[(w2, word)] > 0:

        return bigram_probability(w2, word)

    # Backoff to unigram
    elif unigram[word] > 0:

        return unigram_probability(word)

    return 0


# --------------------------------
# Deleted Interpolation
# --------------------------------

def interpolation_probability(w1, w2, word):

    lambda1 = 0.2
    lambda2 = 0.3
    lambda3 = 0.5

    p1 = unigram_probability(word)

    p2 = bigram_probability(w2, word)

    p3 = trigram_probability(w1, w2, word)

    probability = (
        lambda1 * p1 +
        lambda2 * p2 +
        lambda3 * p3
    )

    return probability


# --------------------------------
# Get Candidate Words
# --------------------------------

vocabulary = list(unigram.keys())


# --------------------------------
# Prediction Function
# --------------------------------

def predict(sentence):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    if len(words) < 2:

        print("Please enter at least two words.")
        return

    w1 = words[-2]
    w2 = words[-1]

    print("\nPrevious words:", w1, w2)

    unsmoothed = []
    backoff = []
    interpolation = []

    for word in vocabulary:

        p1 = unsmoothed_prediction(w1, w2, word)
        p2 = backoff_probability(w1, w2, word)
        p3 = interpolation_probability(w1, w2, word)

        if p1 > 0:
            unsmoothed.append((word, p1))

        if p2 > 0:
            backoff.append((word, p2))

        if p3 > 0:
            interpolation.append((word, p3))

    unsmoothed.sort(key=lambda x: x[1], reverse=True)
    backoff.sort(key=lambda x: x[1], reverse=True)
    interpolation.sort(key=lambda x: x[1], reverse=True)

    print("\nUNSMOOTHED TRIGRAM MODEL")

    if unsmoothed:
        for word, probability in unsmoothed[:5]:
            print(word, "Probability =", round(probability, 4))
    else:
        print("No prediction. Trigram probability is zero.")

    print("\nBACKOFF MODEL")

    for word, probability in backoff[:5]:
        print(word, "Probability =", round(probability, 4))

    print("\nDELETED INTERPOLATION MODEL")

    for word, probability in interpolation[:5]:
        print(word, "Probability =", round(probability, 4))

    print("\nBEST PREDICTIONS")

    print("Unsmoothed:",
          unsmoothed[0][0] if unsmoothed else "None")

    print("Backoff:",
          backoff[0][0] if backoff else "None")

    print("Deleted Interpolation:",
          interpolation[0][0] if interpolation else "None")


# --------------------------------
# Main Program
# --------------------------------

print("======================================")
print("SMOOTHING AND BACKOFF LANGUAGE MODEL")
print("======================================")

sentence = input("\nEnter an incomplete sentence: ")

predict(sentence)


# --------------------------------
# Zero Probability Demonstration
# --------------------------------

print("\n======================================")
print("ZERO PROBABILITY TEST")
print("======================================")

p = trigram_probability(
    "student",
    "is",
    "elephant"
)

print("Trigram: student is elephant")
print("Unsmoothed Probability:", p)

if p == 0:
    print("The trigram is unseen in the training corpus.")


print("\n======================================")
print("PROGRAM COMPLETED")
print("======================================")
