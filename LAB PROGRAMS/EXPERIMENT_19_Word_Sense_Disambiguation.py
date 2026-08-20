import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

# Input sentence
sentence = input("Enter a sentence: ")

# Word to disambiguate
word = input("Enter the word to find its meaning: ")

# Tokenize the sentence
context = word_tokenize(sentence)

# Apply Lesk Algorithm
sense = lesk(context, word)

# Display result
if sense:
    print("\nWord:", word)
    print("Sense:", sense)
    print("Definition:", sense.definition())

    print("\nExample sentences:")
    for example in sense.examples():
        print("-", example)
else:
    print("\nNo suitable sense found for the word.")