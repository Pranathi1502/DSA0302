# Query data
queries = {
    "Q1": ("ACTIVATE", "Roaming", "Activate Roaming"),
    "Q2": ("DEACTIVATE", "CallerTune", "Deactivate Caller Tune"),
    "Q3": ("QUERY", "DataBalance", "Query Data Balance"),
    "Q4": ("ACTIVATE", "5GService", "Activate 5G Service")
}

# Predicted intents
predicted = {
    "Q1": "Activate Roaming",
    "Q2": "Deactivate Caller Tune",   # Corrected
    "Q3": "Query Data Balance",
    "Q4": "Activate 5G Service"
}

# Check each query
for q, (action, obj, intent) in queries.items():

    # Logical representation
    representation = f"{action}({obj}, Customer)"

    # Compare actual and predicted intent
    result = "Correct" if intent == predicted[q] else "Incorrect"

    print(q, ":", representation, "->", result)