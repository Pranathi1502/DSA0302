import re
from collections import Counter

# ---------------------------------------
# TRAINING DATA
# ---------------------------------------

training_data = [
    ("the", "DT"),
    ("student", "NN"),
    ("is", "VBZ"),
    ("studying", "VBG"),
    ("natural", "JJ"),
    ("language", "NN"),
    ("processing", "NN"),

    ("the", "DT"),
    ("student", "NN"),
    ("reads", "VBZ"),
    ("a", "DT"),
    ("book", "NN"),

    ("the", "DT"),
    ("teacher", "NN"),
    ("teaches", "VBZ"),
    ("english", "NN"),

    ("the", "DT"),
    ("student", "NN"),
    ("learns", "VBZ"),
    ("python", "NN"),

    ("she", "PRP"),
    ("is", "VBZ"),
    ("writing", "VBG"),
    ("an", "DT"),
    ("assignment", "NN"),

    ("he", "PRP"),
    ("is", "VBZ"),
    ("reading", "VBG"),
    ("the", "DT"),
    ("book", "NN"),

    ("students", "NNS"),
    ("are", "VBP"),
    ("learning", "VBG"),
    ("quickly", "RB"),

    ("the", "DT"),
    ("smart", "JJ"),
    ("student", "NN"),
    ("works", "VBZ"),
    ("carefully", "RB"),

    ("the", "DT"),
    ("boy", "NN"),
    ("plays", "VBZ"),
    ("football", "NN"),

    ("the", "DT"),
    ("girl", "NN"),
    ("likes", "VBZ"),
    ("music", "NN"),

    ("they", "PRP"),
    ("are", "VBP"),
    ("playing", "VBG"),
    ("football", "NN"),

    ("we", "PRP"),
    ("are", "VBP"),
    ("learning", "VBG"),
    ("english", "NN")
]


# ---------------------------------------
# LEXICAL DICTIONARY
# ---------------------------------------

lexicon = {
    "the": "DT",
    "a": "DT",
    "an": "DT",

    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "language": "NN",
    "processing": "NN",
    "python": "NN",
    "english": "NN",
    "assignment": "NN",
    "boy": "NN",
    "girl": "NN",
    "football": "NN",
    "music": "NN",

    "students": "NNS",

    "he": "PRP",
    "she": "PRP",
    "they": "PRP",
    "we": "PRP",
    "i": "PRP",

    "is": "VBZ",
    "reads": "VBZ",
    "teaches": "VBZ",
    "learns": "VBZ",
    "works": "VBZ",
    "plays": "VBZ",
    "likes": "VBZ",

    "are": "VBP",
    "am": "VBP",

    "studying": "VBG",
    "writing": "VBG",
    "reading": "VBG",
    "learning": "VBG",
    "playing": "VBG",

    "natural": "JJ",
    "smart": "JJ",

    "quickly": "RB",
    "carefully": "RB",

    "in": "IN",
    "on": "IN",
    "at": "IN",
    "with": "IN",
    "for": "IN",

    "and": "CC",
    "but": "CC",
    "or": "CC"
}


# ---------------------------------------
# RULE-BASED POS TAGGER
# ---------------------------------------

def rule_based_tagger(sentence):

    words = re.findall(r"[a-z]+", sentence.lower())

    result = []

    for word in words:

        if word in lexicon:
            tag = lexicon[word]

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("s"):
            tag = "NNS"

        elif word.endswith(("ous", "ful", "ive", "al")):
            tag = "JJ"

        else:
            tag = "NN"

        result.append((word, tag))

    return result


# ---------------------------------------
# BUILD STOCHASTIC MODEL
# ---------------------------------------

word_tag_count = Counter()
tag_count = Counter()
transition_count = Counter()

for word, tag in training_data:

    word_tag_count[(word, tag)] += 1
    tag_count[tag] += 1


for i in range(len(training_data) - 1):

    current_tag = training_data[i][1]
    next_tag = training_data[i + 1][1]

    transition_count[(current_tag, next_tag)] += 1


tags = list(tag_count.keys())


# ---------------------------------------
# STOCHASTIC POS TAGGER
# ---------------------------------------

def stochastic_tagger(sentence):

    words = re.findall(r"[a-z]+", sentence.lower())

    result = []

    previous_tag = None

    for word in words:

        best_tag = "NN"
        best_score = -1

        for tag in tags:

            # Emission probability
            emission = (
                word_tag_count[(word, tag)] + 1
            ) / (
                tag_count[tag] + len(lexicon)
            )

            # Transition probability
            if previous_tag is None:

                transition = 1 / len(tags)

            else:

                total_transitions = sum(
                    transition_count[(previous_tag, t)]
                    for t in tags
                )

                transition = (
                    transition_count[
                        (previous_tag, tag)
                    ] + 1
                ) / (
                    total_transitions + len(tags)
                )

            score = emission * transition

            if score > best_score:

                best_score = score
                best_tag = tag

        result.append((word, best_tag))

        previous_tag = best_tag

    return result


# ---------------------------------------
# TRANSFORMATION-BASED TAGGER
# ---------------------------------------

def transformation_based_tagger(sentence):

    result = rule_based_tagger(sentence)

    for i in range(len(result)):

        word, tag = result[i]

        previous_tag = ""

        previous_word = ""

        if i > 0:
            previous_word = result[i - 1][0]
            previous_tag = result[i - 1][1]

        # Rule: Pronoun + unknown noun -> Verb
        if previous_tag == "PRP" and tag == "NN":
            tag = "VB"

        # Rule: Auxiliary + ing word -> VBG
        if previous_word in ["is", "are", "am"]:
            if word.endswith("ing"):
                tag = "VBG"

        # Rule: Words ending in ly -> Adverb
        if word.endswith("ly"):
            tag = "RB"

        # Rule: Determiner + adjective + noun
        if previous_tag == "JJ" and tag == "NN":
            tag = "NN"

        result[i] = (word, tag)

    return result


# ---------------------------------------
# DISPLAY FUNCTION
# ---------------------------------------

def display_result(title, result):

    print("\n" + title)
    print("-" * 35)

    for word, tag in result:

        print(word + " -> " + tag)


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

print("======================================")
print("PART-OF-SPEECH TAGGING SYSTEM")
print("======================================")

print("\nPenn Treebank POS Tagging")

sentence = input("\nEnter an English sentence: ")

# Rule-Based
rule_result = rule_based_tagger(sentence)

# Stochastic
stochastic_result = stochastic_tagger(sentence)

# Transformation-Based
transformation_result = transformation_based_tagger(sentence)


# ---------------------------------------
# DISPLAY RESULTS
# ---------------------------------------

display_result(
    "RULE-BASED POS TAGGING",
    rule_result
)

display_result(
    "STOCHASTIC POS TAGGING",
    stochastic_result
)

display_result(
    "TRANSFORMATION-BASED POS TAGGING",
    transformation_result
)


# ---------------------------------------
# COMPARISON
# ---------------------------------------

print("\n======================================")
print("COMPARISON OF THREE METHODS")
print("======================================")

print("\nRule-Based:")
for word, tag in rule_result:
    print(word + "/" + tag, end=" ")

print("\n\nStochastic:")
for word, tag in stochastic_result:
    print(word + "/" + tag, end=" ")

print("\n\nTransformation-Based:")
for word, tag in transformation_result:
    print(word + "/" + tag, end=" ")


# ---------------------------------------
# PENN TREEBANK TAGSET
# ---------------------------------------

print("\n\n======================================")
print("PENN TREEBANK TAGSET")
print("======================================")

print("DT  - Determiner")
print("NN  - Singular Noun")
print("NNS - Plural Noun")
print("VB  - Base Verb")
print("VBD - Past Tense Verb")
print("VBG - Gerund / Present Participle")
print("VBZ - Third Person Singular Verb")
print("VBP - Non-Third Person Singular Verb")
print("JJ  - Adjective")
print("RB  - Adverb")
print("PRP - Personal Pronoun")
print("IN  - Preposition")
print("CC  - Coordinating Conjunction")


# ---------------------------------------
# FINAL MESSAGE
# ---------------------------------------

print("\n======================================")
print("PROGRAM COMPLETED")
print("======================================")
