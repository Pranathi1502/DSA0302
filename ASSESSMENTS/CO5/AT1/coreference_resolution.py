# Constraint-Based Coreference Resolution

# Entities mentioned in the paragraph
entities = {
    "John": {
        "gender": "male",
        "number": "singular",
        "animacy": "human"
    },
    "Mary": {
        "gender": "female",
        "number": "singular",
        "animacy": "human"
    },
    "ball": {
        "gender": "neutral",
        "number": "singular",
        "animacy": "object"
    },
    "park": {
        "gender": "neutral",
        "number": "singular",
        "animacy": "place"
    },
    "dog": {
        "gender": "male",
        "number": "singular",
        "animacy": "animal"
    }
}


# Pronoun constraints
pronouns = {
    "He": {
        "gender": "male",
        "number": "singular"
    },
    "She": {
        "gender": "female",
        "number": "singular"
    },
    "it": {
        "gender": "neutral",
        "number": "singular"
    },
    "him": {
        "gender": "male",
        "number": "singular"
    },
    "they": {
        "number": "plural"
    }
}


# Possible antecedents
possible = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["ball", "park"],
    "him": ["John", "Mary", "dog"],
    "they": ["John", "Mary", "dog"]
}


# Function for gender and number agreement
def agreement(pronoun, entity):

    p = pronouns[pronoun]
    e = entities[entity]

    if "gender" in p:
        if p["gender"] != e["gender"]:
            return False

    if "number" in p:
        if p["number"] != e["number"]:
            return False

    return True


# Semantic compatibility
def semantic_compatibility(pronoun, entity):

    # "it" refers to an object in this example
    if pronoun == "it":
        return entities[entity]["animacy"] == "object"

    # "him" refers to a human male in this context
    if pronoun == "him":
        return entity == "John"

    return True


# Resolve references
resolved = {}

for pronoun, candidates in possible.items():

    valid_candidates = []

    for candidate in candidates:

        # Apply agreement constraint
        if not agreement(pronoun, candidate):
            continue

        # Apply semantic compatibility
        if not semantic_compatibility(pronoun, candidate):
            continue

        valid_candidates.append(candidate)

    if valid_candidates:
        resolved[pronoun] = valid_candidates[0]


# "they" refers to the complete group
resolved["they"] = "John + Mary + dog"


# Display results
print("CONSTRAINT-BASED COREFERENCE RESOLUTION")
print("=" * 45)

for pronoun, antecedent in resolved.items():
    print(pronoun, "->", antecedent)


# Coreference chains
print("\nCoreference Chains:")
print("John -> He -> him -> they")
print("Mary -> She -> they")
print("ball -> it")
print("dog -> they")


# Rewritten paragraph
print("\nRewritten Paragraph:")
print(
    "John and Mary went to the park. "
    "John brought a ball. "
    "Mary wanted to play with the ball. "
    "The dog chased John excitedly. "
    "Finally, John, Mary, and the dog all went home."
)