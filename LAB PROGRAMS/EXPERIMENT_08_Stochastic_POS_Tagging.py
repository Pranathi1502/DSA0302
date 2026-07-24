# ==========================================================
# Experiment 08
# Aim:
# Implement a Simple Stochastic POS Tagging Algorithm.
# ==========================================================

import random

words = ["book", "play", "computer", "student", "run"]

possible_tags = ["NN", "VB"]

print("Stochastic POS Tagging\n")

for word in words:
    tag = random.choice(possible_tags)
    print(word, ":", tag)

print("\nExperiment Completed Successfully.")