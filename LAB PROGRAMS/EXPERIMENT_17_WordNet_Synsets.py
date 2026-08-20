from nltk.corpus import wordnet

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

print("\nWordNet Synsets:\n")

if synsets:
    for synset in synsets:
        print("Synset:", synset.name())
        print("Definition:", synset.definition())
        print("Example:", synset.examples())
        print()
else:
    print("No synsets found.")