import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

# Download required NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input text
text = input("Enter a text: ")

# Pronouns to resolve
pronouns = {
    "he", "she", "him", "her",
    "they", "them", "it", "its"
}

# Store previously found nouns
previous_nouns = []

# Split text into sentences
sentences = sent_tokenize(text)

print("\nReference Resolution Results:\n")

for sentence in sentences:

    # Tokenize and POS tag the sentence
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    for word, tag in tagged_words:

        # Check if the word is a noun
        if tag.startswith("NN"):
            previous_nouns.append(word)

        # Check if the word is a pronoun
        elif word.lower() in pronouns:

            if previous_nouns:
                # Resolve pronoun to the most recent noun
                reference = previous_nouns[-1]

                print(f"Pronoun: {word}")
                print(f"Refers to: {reference}\n")

            else:
                print(f"Pronoun: {word}")
                print("Refers to: Unable to resolve\n")