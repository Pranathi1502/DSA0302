import re

rules = [
    (r"^(the|a) (boy|girl|cat|dog) (runs|plays|eats)$", "Singular"),
    (r"^(the) (boys|girls|cats|dogs) (run|play|eat)$", "Plural")
]

sentence = input("Enter a sentence: ").lower().strip()

for pattern, form in rules:
    if re.match(pattern, sentence):
        print("\nAgreement: Valid")
        print("Number: " + form)
        break
else:
    print("\nAgreement: Invalid")