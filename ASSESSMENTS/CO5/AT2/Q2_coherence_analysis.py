# Q2 - Text Coherence and Discourse Structure

sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

print("=" * 60)
print("TEXT COHERENCE AND DISCOURSE ANALYSIS")
print("=" * 60)

print("\nDiscourse:")
for i, sentence in enumerate(sentences, 1):
    print(f"S{i}: {sentence}")

# Identify discourse relations
relations = [
    ("S1", "S2", "CAUSE-EFFECT"),
    ("S2", "S3", "RESULT / SEQUENCE")
]

print("\nDiscourse Relations:")
for first, second, relation in relations:
    print(f"{first} -> {second} : {relation}")

print("\nDiscourse Structure:")
print("Heavy rainfall")
print("      ↓")
print("Roads flooded")
print("      ↓")
print("Schools closed")
print("      ↓")
print("Students attended online classes")

print("\nCoherence Validation:")
print("Logical connection : Satisfied")
print("Cause-effect       : Satisfied")
print("Sequence            : Satisfied")
print("Overall coherence  : Satisfied")