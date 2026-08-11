import math

# Sentences
sentences = [
    "Book a flight ticket now",
    "This book is interesting"
]

# Lexicon
lexicon = {
    "book": "NN",
    "a": "DT",
    "flight": "NN",
    "ticket": "NN",
    "now": "RB",
    "this": "DT",
    "is": "VBZ",
    "interesting": "JJ"
}

# Rule-Based POS Tagger
def rule_based(sentence):
    words = sentence.lower().split()
    result = []

    for i, w in enumerate(words):

        # "Book" at the beginning followed by "a" is a verb
        if w == "book" and i == 0 and len(words) > 1 and words[i + 1] == "a":
            tag = "VB"

        elif w in lexicon:
            tag = lexicon[w]

        else:
            tag = "NN"

        result.append((w, tag))

    return result


print("CASE STUDY 2")

# Rule-Based POS Tagging
for sentence in sentences:

    print("\nSentence:", sentence)

    for word, tag in rule_based(sentence):
        print(word, "->", tag)


# HMM Probability
p_vb = 0.5 * 0.6
p_nn = 0.5 * 0.4

print("\nHMM Probability")
print("P(book,VB) =", round(p_vb, 4))
print("P(book,NN) =", round(p_nn, 4))

if p_vb > p_nn:
    print("HMM Prediction: VB")
else:
    print("HMM Prediction: NN")


# Penn Treebank Tags
print("\nPenn Treebank Tags")
print("VB  = Verb")
print("NN  = Noun")
print("DT  = Determiner")
print("RB  = Adverb")
print("VBZ = 3rd Person Singular Verb")
print("JJ  = Adjective")
