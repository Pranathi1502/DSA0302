# ==========================================================
# Experiment 08
# Aim: Simple Stochastic POS Tagging.
# ==========================================================

import random

words = ["book", "play", "run", "computer", "student"]

tags = ["NN", "VB"]

print("Stochastic POS Tagging:\n")

for word in words:
    tag = random.choice(tags)
    print(word, ":", tag)

print("\nStochastic POS Tagging Completed Successfully.")