# Probabilistic Semantic Interpretation of a Banking Query

query = "Show me the transactions with the card from last month."

print("User Query:")
print(query)

# Possible interpretations with probability scores
interpretations = {
    "Transaction history for the card during last month": 0.90,
    "Transactions associated with a card from last month": 0.60
}

# Select the interpretation with the highest probability
best = max(interpretations, key=interpretations.get)
probability = interpretations[best]

# Extract semantic information
intent = "Transaction History"
card = "User's Card"
time_period = "Last Month"

# Display all possible interpretations
print("\nPossible Interpretations:")

for meaning, score in interpretations.items():
    print(f"{meaning} -> {score}")

# Display best interpretation
print("\nBest Interpretation:")
print(best)
print("Probability:", probability)

# Display semantic representation
print("\nSemantic Representation:")
print(f"Intent = {intent}")
print(f"Card = {card}")
print(f"Time Period = {time_period}")

# Display predicate representation
print("\nPredicate Representation:")
print("ShowTransactions(User, Card, LastMonth)")