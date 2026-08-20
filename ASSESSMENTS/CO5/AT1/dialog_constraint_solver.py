# Constraint-Based Dialog Generation
# Q2 - Advise + Encourage

responses = [
    "Since you are unable to concentrate on your important exam, "
    "take a short break and then return with a clear focus. "
    "You can study one topic at a time, which will help you feel more confident about the exam.",

    "Because you have an important exam tomorrow, take a short break "
    "to refresh your mind and improve your focus. "
    "You can concentrate better after the break, so stay positive and feel confident about your preparation.",

    "If you are finding it difficult to concentrate, take a short break "
    "and remove distractions before studying for the exam. "
    "This can improve your focus and help you feel more confident about tomorrow."
]

# Required keywords
keywords = ["focus", "break", "confident"]

# Check constraints
def check_constraints(response):

    result = {}

    # 1. Entity coherence
    entities = ["exam", "concentrate", "you"]
    result["Entity Coherence"] = all(
        entity in response.lower() for entity in entities
    )

    # 2. Discourse relation
    cause_effect_words = [
        "since", "because", "if", "so", "therefore", "which", "can"
    ]

    result["Discourse Relation"] = any(
        word in response.lower() for word in cause_effect_words
    )

    # 3. Keyword constraint
    keyword_count = sum(
        keyword in response.lower()
        for keyword in keywords
    )

    result["Required Keywords"] = keyword_count >= 2

    # 4. Response length
    sentence_count = response.count(".")
    result["Response Length"] = 2 <= sentence_count <= 3

    # 5. Positive tone
    positive_words = [
        "confident",
        "positive",
        "improve",
        "help",
        "clear",
        "refresh"
    ]

    result["Positive Tone"] = any(
        word in response.lower()
        for word in positive_words
    )

    # 6. Logical consistency
    negative_words = [
        "fail",
        "bad",
        "cannot pass",
        "hopeless"
    ]

    result["Logical Consistency"] = not any(
        word in response.lower()
        for word in negative_words
    )

    return result


# Evaluate all responses
print("=" * 60)
print("CONSTRAINT-BASED DIALOG GENERATION")
print("=" * 60)

scores = []

for i, response in enumerate(responses, start=1):

    print(f"\nRESPONSE {i}")
    print("-" * 60)
    print(response)

    results = check_constraints(response)

    score = 0

    print("\nConstraint Evaluation:")

    for constraint, satisfied in results.items():

        if satisfied:
            print(f"{constraint}: Satisfied")
            score += 1
        else:
            print(f"{constraint}: Not Satisfied")

    scores.append(score)

    print(f"Score: {score}/{len(results)}")


# Select the best response
best_index = scores.index(max(scores))

print("\n" + "=" * 60)
print("BEST RESPONSE")
print("=" * 60)

print(f"\nResponse {best_index + 1}:")
print(responses[best_index])

print(f"\nBest Score: {scores[best_index]}/{len(check_constraints(responses[best_index]))}")

print("\nReason:")
print("The selected response satisfies the required constraints,")
print("maintains entity coherence, uses a cause-effect relation,")
print("contains the required keywords, and provides positive encouragement.")