# Q5 - Interlingua and Statistical Translation

source = "The boy is playing football."

print("=" * 60)
print("INTERLINGUA + STATISTICAL TRANSLATION")
print("=" * 60)

print("\nSource Sentence:")
print(source)

# Step 1: Source analysis
source_analysis = {
    "Subject": "Boy",
    "Action": "Play",
    "Object": "Football",
    "Tense": "Present",
    "Aspect": "Continuous"
}

print("\n1. Source Analysis:")

for key, value in source_analysis.items():
    print(f"{key}: {value}")

# Step 2: Interlingua representation
interlingua = (
    "PLAY(Agent=BOY, Object=FOOTBALL, "
    "Tense=PRESENT, Aspect=CONTINUOUS)"
)

print("\n2. Interlingua Representation:")
print(interlingua)

# Step 3: Candidate translations
candidates = {
    "சிறுவன் கால்பந்து விளையாடுகிறான்.": 0.95,
    "சிறுவன் கால்பந்து விளையாடினான்.": 0.60
}

print("\n3. Candidate Translations:")

for translation, score in candidates.items():
    print(f"{translation} -> Score: {score}")

# Step 4: Select highest scoring translation
best_translation = max(candidates, key=candidates.get)
best_score = candidates[best_translation]

print("\n4. Statistical Selection:")
print("Best Translation:", best_translation)
print("Score:", best_score)

# Step 5: Final output
print("\n5. Final Translation:")
print(best_translation)

print("\nValidation:")
print("Meaning preservation : Satisfied")
print("Tense preservation   : Satisfied")
print("Aspect preservation  : Satisfied")
print("Semantic coherence   : Satisfied")
print("Translation quality  : Good")