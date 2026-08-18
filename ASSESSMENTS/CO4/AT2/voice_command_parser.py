from nltk import CFG
from nltk.parse import RecursiveDescentParser, EarleyChartParser

# Define grammar
grammar = CFG.fromstring("""
S -> VP
VP -> V NP
NP -> Det N PP
NP -> Det N
NP -> N PP
NP -> N
PP -> P NP
V -> 'book'
Det -> 'a'
N -> 'flight' | 'Delhi' | 'seat' | 'window'
P -> 'to' | 'with'
""")

# Voice assistant command
sentence = "book a flight to Delhi with a window seat".split()

print("Command:")
print(" ".join(sentence))

# Top-Down Parsing
print("\nTop-Down Parsing:")

top_down = RecursiveDescentParser(grammar)
count = 0

for tree in top_down.parse(sentence):
    print(tree)
    count += 1

    if count == 1:
        break

# Earley Parsing
print("\nEarley Parsing:")

earley = EarleyChartParser(grammar)
count = 0

for tree in earley.parse(sentence):
    print(tree)
    count += 1

    if count == 1:
        break

# Semantic Representation
print("\nSemantic Representation:")
print("BookFlight(User, Delhi, WindowSeat)")