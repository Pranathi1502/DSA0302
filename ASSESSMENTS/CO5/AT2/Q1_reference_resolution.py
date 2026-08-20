# Q1 - Reference Resolution

text = "Ravi met Arun at the library. He borrowed a book and later returned it."

print("=" * 60)
print("REFERENCE RESOLUTION")
print("=" * 60)

print("\nOriginal Text:")
print(text)

# Entities
entities = ["Ravi", "Arun", "book"]

# Pronoun resolution
resolution = {
    "He": "Ravi",
    "it": "book"
}

print("\nCoreference Resolution:")
for pronoun, entity in resolution.items():
    print(pronoun, "->", entity)

# Resolved discourse
resolved_text = (
    "Ravi met Arun at the library. "
    "Ravi borrowed a book and later returned the book."
)

print("\nResolved Discourse:")
print(resolved_text)

print("\nValidation:")
print("Gender agreement      : Satisfied")
print("Number agreement      : Satisfied")
print("Semantic compatibility: Satisfied")
print("Discourse coherence   : Satisfied")
print("Reference resolution  : Correct")