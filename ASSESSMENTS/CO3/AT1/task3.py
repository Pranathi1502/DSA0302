import re
import math
from collections import Counter

# --------------------------------
# Training Corpus
# --------------------------------

training_corpus = """
The student is studying natural language processing.
The student is learning Python programming.
The student is reading a book.
The student is writing an assignment.
The teacher is teaching natural language processing.
The teacher is explaining the topic.
The student is learning machine learning.
The student studies machine learning.
Natural language processing is interesting.
Python programming is useful.
Machine learning is useful.
The book is useful for students.
The student is practicing Python programming.
The student is solving problems.
"""

# --------------------------------
# Test Corpus
# --------------------------------

test_corpus = """
The student is learning Python.
The student is reading a book.
The teacher is teaching the student.
Machine learning is useful.
The student is studying programming.
"""

# --------------------------------
# Tokenization
# --------------------------------

def tokenize(text):
    return re.findall(r'\b[a-z]+\b', text.lower())


train_tokens = tokenize(training_corpus)
test_tokens = tokenize(test_corpus)

print("Training words:", len(train_tokens))
print("Testing words:", len(test_tokens))


# --------------------------------
# Build N-gram Models
# --------------------------------

unigram = Counter(train_tokens)

bigram = Counter()

trigram = Counter()

for i in range(len(train_tokens) - 1):
    bigram[(train_tokens[i], train_tokens[i + 1])] += 1

for i in range(len(train_tokens) - 2):
    trigram[(train_tokens[i], train_tokens[i + 1], train_tokens[i + 2])] += 1


# --------------------------------
# Probability Functions
# --------------------------------

def unigram_probability(word):

    return unigram[word] / len(train_tokens)


def bigram_probability(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# --------------------------------
# Laplace Smoothing
# --------------------------------

vocabulary = set(train_tokens)

V = len(vocabulary)


def smoothed_bigram_probability(w1, w2):

    return (bigram[(w1, w2)] + 1) / (
        unigram[w1] + V
    )


def smoothed_trigram_probability(w1, w2, w3):

    return (trigram[(w1, w2, w3)] + 1) / (
        bigram[(w1, w2)] + V
    )


# --------------------------------
# Entropy Calculation
# --------------------------------

def calculate_entropy(probabilities):

    total = 0

    count = 0

    for p in probabilities:

        if p > 0:

            total += -math.log2(p)

            count += 1

    if count == 0:
        return 0

    return total / count


# --------------------------------
# Unigram Entropy
# --------------------------------

unigram_probs = []

for word in test_tokens:

    p = unigram_probability(word)

    unigram_probs.append(p)


unigram_entropy = calculate_entropy(unigram_probs)


# --------------------------------
# Bigram Entropy
# --------------------------------

bigram_probs = []

for i in range(1, len(test_tokens)):

    w1 = test_tokens[i - 1]
    w2 = test_tokens[i]

    p = bigram_probability(w1, w2)

    bigram_probs.append(p)


bigram_entropy = calculate_entropy(bigram_probs)


# --------------------------------
# Trigram Entropy
# --------------------------------

trigram_probs = []

for i in range(2, len(test_tokens)):

    w1 = test_tokens[i - 2]
    w2 = test_tokens[i - 1]
    w3 = test_tokens[i]

    p = trigram_probability(w1, w2, w3)

    trigram_probs.append(p)


trigram_entropy = calculate_entropy(trigram_probs)


# --------------------------------
# Smoothed Bigram Entropy
# --------------------------------

smoothed_bigram_probs = []

for i in range(1, len(test_tokens)):

    w1 = test_tokens[i - 1]
    w2 = test_tokens[i]

    p = smoothed_bigram_probability(w1, w2)

    smoothed_bigram_probs.append(p)


smoothed_bigram_entropy = calculate_entropy(
    smoothed_bigram_probs
)


# --------------------------------
# Smoothed Trigram Entropy
# --------------------------------

smoothed_trigram_probs = []

for i in range(2, len(test_tokens)):

    w1 = test_tokens[i - 2]
    w2 = test_tokens[i - 1]
    w3 = test_tokens[i]

    p = smoothed_trigram_probability(
        w1, w2, w3
    )

    smoothed_trigram_probs.append(p)


smoothed_trigram_entropy = calculate_entropy(
    smoothed_trigram_probs
)


# --------------------------------
# Display Entropy Results
# --------------------------------

print("\n================================")
print("ENTROPY RESULTS")
print("================================")

print(
    "Unigram Entropy:",
    round(unigram_entropy, 4)
)

print(
    "Bigram Entropy:",
    round(bigram_entropy, 4)
)

print(
    "Trigram Entropy:",
    round(trigram_entropy, 4)
)

print(
    "Smoothed Bigram Entropy:",
    round(smoothed_bigram_entropy, 4)
)

print(
    "Smoothed Trigram Entropy:",
    round(smoothed_trigram_entropy, 4)
)


# --------------------------------
# Next Word Prediction
# --------------------------------

def predict_next_word(sentence):

    words = tokenize(sentence)

    if len(words) < 2:

        print("Enter at least two words.")

        return

    w1 = words[-2]
    w2 = words[-1]

    predictions = []

    for word in vocabulary:

        probability = smoothed_trigram_probability(
            w1, w2, word
        )

        predictions.append(
            (word, probability)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\nNext Word Prediction")

    for word, probability in predictions[:5]:

        print(
            word,
            "Probability =",
            round(probability, 4)
        )


# --------------------------------
# User Prediction
# --------------------------------

print("\n================================")
print("TEXT PREDICTION")
print("================================")

sentence = input(
    "Enter an incomplete sentence: "
)

predict_next_word(sentence)


# --------------------------------
# High and Low Entropy Sequences
# --------------------------------

print("\n================================")
print("ENTROPY INTERPRETATION")
print("================================")

sequences = [
    "the student is learning",
    "the teacher is teaching",
    "machine learning is useful",
    "student elephant computer"
]

for sequence in sequences:

    words = tokenize(sequence)

    probabilities = []

    for i in range(1, len(words)):

        p = smoothed_bigram_probability(
            words[i - 1],
            words[i]
        )

        probabilities.append(p)

    entropy = calculate_entropy(probabilities)

    print(
        sequence,
        "-> Entropy =",
        round(entropy, 4)
    )


# --------------------------------
# Final Interpretation
# --------------------------------

print("\n================================")
print("FINAL INTERPRETATION")
print("================================")

print(
    "Lower entropy means the next word is more predictable."
)

print(
    "Higher entropy means greater uncertainty."
)

print(
    "Smoothing prevents zero probability for unseen N-grams."
)

print(
    "Therefore, smoothing provides more reliable probability estimates."
)

print("\nPROGRAM COMPLETED")
