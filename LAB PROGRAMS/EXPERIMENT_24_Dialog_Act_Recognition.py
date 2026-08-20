# Experiment 24: Dialog Act Recognition

def recognize_dialog_act(sentence):
    sentence_lower = sentence.lower().strip()

    # Greeting
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon"]
    if any(word in sentence_lower for word in greetings):
        return "Greeting"

    # Farewell
    farewells = ["bye", "goodbye", "see you", "take care"]
    if any(word in sentence_lower for word in farewells):
        return "Farewell"

    # Thanks
    thanks = ["thank you", "thanks", "thank"]
    if any(word in sentence_lower for word in thanks):
        return "Thanking"

    # Question
    if sentence.endswith("?") or sentence_lower.startswith(
        ("what", "when", "where", "why", "who", "how", "do", "does", "can", "could")
    ):
        return "Question"

    # Request
    request_words = ["please", "could you", "can you", "would you"]
    if any(word in sentence_lower for word in request_words):
        return "Request"

    # Default
    return "Statement"


# Input conversation
conversation = input("Enter the conversation: ")

# Split conversation into sentences
sentences = conversation.split(".")

print("\nDialog Act Recognition Results:\n")

for sentence in sentences:
    sentence = sentence.strip()

    if sentence:
        dialog_act = recognize_dialog_act(sentence)
        print("Sentence:", sentence)
        print("Dialog Act:", dialog_act)
        print()