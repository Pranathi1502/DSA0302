import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

# Define CFG grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP | V
Det -> 'The'
N -> 'student'
V -> 'wants'
""")

# Create Earley parser
parser = EarleyChartParser(grammar)

# Input sentence
sentence = "The student wants".split()

# Parse the sentence
print("Earley Parsing Result:")

for tree in parser.parse(sentence):
    print(tree)