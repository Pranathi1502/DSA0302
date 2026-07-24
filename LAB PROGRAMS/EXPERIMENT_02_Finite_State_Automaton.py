# ==========================================================
# Experiment 02
# Aim:
# Implement a Finite State Automaton to recognize
# strings ending with 'ab'.
# ==========================================================

def finite_state_automaton(string):
    if string.endswith("ab"):
        return "Accepted"
    else:
        return "Rejected"

strings = ["ab", "aab", "aaab", "cab", "abab", "abc", "ba"]

print("Finite State Automaton\n")

for s in strings:
    print(s, ":", finite_state_automaton(s))

print("\nExperiment Completed Successfully.")