import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "The student reads a book."

# Process the sentence
doc = nlp(sentence)

# Display dependency relations
print("Dependency Relations:")

for token in doc:
    print(token.text, "->", token.dep_, "->", token.head.text)