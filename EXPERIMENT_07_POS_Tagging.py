# ==========================================================
# Experiment 07
# Aim: Perform Part-of-Speech Tagging using NLTK.
# ==========================================================

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "The cat is sitting on the mat."

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print("Words and their POS Tags:\n")

for word, tag in tags:
    print(word, ":", tag)

print("\nPOS Tagging Completed Successfully.")