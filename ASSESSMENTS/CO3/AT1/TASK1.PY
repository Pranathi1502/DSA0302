import re
from collections import Counter

# -------------------------------
# 1. Training Corpus
# -------------------------------
corpus = """
The student is studying natural language processing.
The student is learning Python programming.
The student is reading a book.
The student is writing an assignment.
The teacher is teaching natural language processing.
The teacher is explaining the topic.
The teacher gives the student a book.
The student learns machine learning.
The student studies machine learning.
Students are learning Python.
Students are reading books.
Natural language processing is interesting.
Python programming is interesting.
Machine learning is useful.
The book is useful for students.
"""

# -------------------------------
# 2. Preprocessing and Tokenization
# -------------------------------
corpus = corpus.lower()

sentences = corpus.split(".")

tokens = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)
    tokens.extend(words)

print("Total words:", len(tokens))

# -------------------------------
# 3. Create N-gram Counts
# -------------------------------

unigram = Counter(tokens)

bigram = Counter()
trigram = Counter()

for i in range(len(tokens) - 1):
    bigram[(tokens[i], tokens[i + 1])] += 1

for i in range(len(tokens) - 2):
    trigram[(tokens[i], tokens[i + 1], tokens[i + 2])] += 1


# -------------------------------
# 4. Probability Functions
# -------------------------------

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


# -------------------------------
# 5. Select N
# -------------------------------

print("\nChoose N:")
print("1 - Unigram")
print("2 - Bigram")
print("3 - Trigram")

n = int(input("Enter N: "))

if n not in [1, 2, 3]:
    print("Please enter only 1, 2 or 3.")
    exit()


# -------------------------------
# 6. Display Frequency and Probability
# -------------------------------

if n == 1:

    print("\n--- UNIGRAM FREQUENCY AND PROBABILITY ---")

    for word, count in unigram.most_common(15):
        probability = unigram_probability(word)

        print(word,
              "Count =", count,
              "Probability =", round(probability, 4))


elif n == 2:

    print("\n--- BIGRAM FREQUENCY AND PROBABILITY ---")

    for (w1, w2), count in bigram.most_common(15):

        probability = bigram_probability(w1, w2)

        print((w1, w2),
              "Count =", count,
              "Probability =", round(probability, 4))


else:

    print("\n--- TRIGRAM FREQUENCY AND PROBABILITY ---")

    for (w1, w2, w3), count in trigram.most_common(15):

        probability = trigram_probability(w1, w2, w3)

        print((w1, w2, w3),
              "Count =", count,
              "Probability =", round(probability, 4))


# -------------------------------
# 7. Next Word Prediction
# -------------------------------

def predict_next_word(sentence, n):

    words = re.findall(r'\b[a-z]+\b', sentence.lower())

    predictions = []

    # -------- UNIGRAM --------
    if n == 1:

        for word, count in unigram.items():

            probability = unigram_probability(word)

            predictions.append((word, probability))

    # -------- BIGRAM --------
    elif n == 2:

        if len(words) < 1:
            return []

        previous_word = words[-1]

        for (w1, w2), count in bigram.items():

            if w1 == previous_word:

                probability = bigram_probability(w1, w2)

                predictions.append((w2, probability))

    # -------- TRIGRAM --------
    elif n == 3:

        if len(words) < 2:
            return []

        w1 = words[-2]
        w2 = words[-1]

        for (a, b, c), count in trigram.items():

            if a == w1 and b == w2:

                probability = trigram_probability(a, b, c)

                predictions.append((c, probability))

    predictions.sort(key=lambda x: x[1], reverse=True)

    return predictions[:5]


# -------------------------------
# 8. User Input
# -------------------------------

print("\n--------------------------------")
sentence = input("Enter incomplete sentence: ")
print("--------------------------------")

predictions = predict_next_word(sentence, n)


# -------------------------------
# 9. Display Top-5 Predictions
# -------------------------------

print("\nTOP-5 NEXT WORD PREDICTIONS")

if len(predictions) == 0:

    print("No prediction found.")
    print("The N-gram is unseen in the training corpus.")

else:

    for i, (word, probability) in enumerate(predictions, 1):

        print(i, ".", word,
              "Probability =", round(probability, 4))


# -------------------------------
# 10. Demonstrate Zero Probability
# -------------------------------

print("\n--------------------------------")
print("UNSEEN N-GRAM TEST")
print("--------------------------------")

if n == 1:

    word = "elephant"

    probability = unigram_probability(word)

    print("Word:", word)
    print("Probability:", probability)


elif n == 2:

    w1 = "student"
    w2 = "elephant"

    probability = bigram_probability(w1, w2)

    print("Bigram:", w1, w2)
    print("Probability:", probability)


else:

    w1 = "student"
    w2 = "is"
    w3 = "elephant"

    probability = trigram_probability(w1, w2, w3)

    print("Trigram:", w1, w2, w3)
    print("Probability:", probability)


# -------------------------------
# 11. Simple Test Cases
# -------------------------------

print("\n================================")
print("TEST CASES")
print("================================")

test_cases = [
    "the student",
    "the teacher",
    "machine learning",
    "the book"
]

for test in test_cases:

    result = predict_next_word(test, n)

    print("\nInput:", test)

    if result:

        print("Predicted word:", result[0][0])
        print("Probability:", round(result[0][1], 4))

    else:

        print("No prediction found.")


print("\n================================")
print("PROGRAM COMPLETED")
print("================================")
