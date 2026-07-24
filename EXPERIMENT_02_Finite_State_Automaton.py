# ==========================================================
# Experiment 02
# Aim:
# Implement a Finite State Automaton (FSA) to recognize
# strings ending with 'ab'.
# ==========================================================

def finite_state_automaton(string):

    # Check whether the string ends with 'ab'
    if string.endswith("ab"):
        return "Accepted"
    else:
        return "Rejected"


# Sample strings
strings = [
    "ab",
    "aab",
    "aaab",
    "cab",
    "abab",
    "abc",
    "ba",
    "baba"
]

print("========== FINITE STATE AUTOMATON ==========\n")

for s in strings:
    result = finite_state_automaton(s)
    print(f"String: {s:6} --> {result}")

print("\nFinite State Automaton Completed Successfully.")