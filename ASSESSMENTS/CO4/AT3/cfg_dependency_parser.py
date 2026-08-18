import nltk
import spacy

# Define CFG grammar
grammar = """
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'The'
N -> 'doctor' | 'medicine'
V -> 'prescribed'
"""

# Create CFG
cfg = nltk.CFG.fromstring(grammar)

# Create Chart Parser
parser = nltk.ChartParser(cfg)

# Input sentence
sentence = "The doctor prescribed medicine".split()

# CFG Parsing
print("CFG Tree:")

for tree in parser.parse(sentence):
    print(tree)

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Perform dependency parsing
doc = nlp("The doctor prescribed medicine")

print("\nDependency Relations:")

for token in doc:
    print(token.text, "->", token.dep_, "->", token.head.text)