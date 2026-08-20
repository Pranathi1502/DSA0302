import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

doc = nlp(text)

print("\nNamed Entities:\n")

if doc.ents:
    for ent in doc.ents:
        print(ent.text, "-->", ent.label_)
else:
    print("No named entities found.")