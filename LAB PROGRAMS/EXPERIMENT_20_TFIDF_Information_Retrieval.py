from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Natural language processing is a branch of artificial intelligence",
    "Machine learning is used in artificial intelligence",
    "Python is widely used for data science and machine learning",
    "Information retrieval helps find relevant documents",
    "TF IDF is used for document ranking in information retrieval"
]

# Get user query
query = input("Enter your search query: ")

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert query into TF-IDF vector
query_vector = vectorizer.transform([query])

# Calculate cosine similarity between query and documents
similarity_scores = cosine_similarity(
    query_vector, tfidf_matrix
).flatten()

# Rank documents based on similarity scores
ranked_results = sorted(
    enumerate(similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\nQuery:", query)
print("\nRanked Documents:")

for index, score in ranked_results:
    print(f"\nDocument {index + 1}")
    print("Text:", documents[index])
    print("Similarity Score:", round(score, 4))