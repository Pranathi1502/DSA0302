# ==========================================================
# Experiment 05
# Aim:
# Implement a basic N-Gram (Bigram) model for text generation.
# ==========================================================

import nltk
from nltk.util import bigrams

# Download tokenizer (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')

# Sample sentence
text = "Natural language processing is very interesting and useful"

# Tokenize the sentence
words = nltk.word_tokenize(text)

print("Original Words:")
print(words)

# Generate Bigrams
bigram_list = list(bigrams(words))

print("\nGenerated Bigrams:")
for bg in bigram_list:
    print(bg)

# Generate simple text using bigrams
print("\nGenerated Text:")

generated_text = words[0]

for pair in bigram_list:
    generated_text += " " + pair[1]

print(generated_text)

print("\nN-Gram Text Generation Completed Successfully.")