import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [1.0]
VP -> V NP [1.0]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'cat' [0.5] | 'dog' [0.5]
V -> 'chased' [0.5] | 'saw' [0.5]
""")

parser = ViterbiParser(grammar)

sentence = input("Enter a sentence: ").lower().split()

print("\nMost Probable Parse Tree:\n")

trees = list(parser.parse(sentence))

if trees:
    tree = trees[0]
    print(tree)
    print("\nProbability:", tree.prob())
else:
    print("No parse tree found.")