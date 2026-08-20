import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK resource
nltk.download('punkt')

# Get input text
text = input("Enter a paragraph: ")

# Split the text into sentences
sentences = sent_tokenize(text)

# Check if there are enough sentences
if len(sentences) < 2:
    print("Please enter at least two sentences.")
else:
    # Convert sentences into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

    similarity_scores = []

    print("\nCoherence Between Consecutive Sentences:\n")

    # Compare consecutive sentences
    for i in range(len(sentences) - 1):
        score = cosine_similarity(
            tfidf_matrix[i],
            tfidf_matrix[i + 1]
        )[0][0]

        similarity_scores.append(score)

        print(f"Sentence {i + 1}: {sentences[i]}")
        print(f"Sentence {i + 2}: {sentences[i + 1]}")
        print("Similarity Score:", round(score, 4))
        print()

    # Calculate average coherence score
    average_coherence = sum(similarity_scores) / len(similarity_scores)

    print("Average Coherence Score:", round(average_coherence, 4))

    # Evaluate coherence
    if average_coherence >= 0.2:
        print("Result: The text is reasonably coherent.")
    else:
        print("Result: The text has low coherence.")