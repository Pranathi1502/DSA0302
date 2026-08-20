import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser
from nltk.corpus import wordnet

# Download required NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Get input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(sentence)

# Perform Part-of-Speech tagging
tagged_words = pos_tag(words)

# Define grammar for noun phrases
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

# Create chunk parser
chunk_parser = RegexpParser(grammar)

# Extract noun phrases
tree = chunk_parser.parse(tagged_words)

print("\nNoun Phrases and Their Meanings:\n")

# Process noun phrases
for subtree in tree.subtrees():
    if subtree.label() == "NP":

        # Extract noun phrase
        noun_phrase = " ".join(word for word, tag in subtree.leaves())

        # Get the main noun (last word in the noun phrase)
        main_noun = subtree.leaves()[-1][0]

        # Find meaning using WordNet
        synsets = wordnet.synsets(main_noun)

        print("Noun Phrase:", noun_phrase)

        if synsets:
            print("Meaning:", synsets[0].definition())
        else:
            print("Meaning: Not found in WordNet")

        print()