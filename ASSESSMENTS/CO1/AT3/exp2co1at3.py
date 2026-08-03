# ==========================================================
# Experiment 02
# Aim:
# Design a Deterministic Finite Automata (DFA) Simulator
# to recognize strings ending with "ab".
# ==========================================================

# DFA Description
states = ['q0', 'q1', 'q2']
alphabet = ['a', 'b']

transition = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}

initial_state = 'q0'
final_state = 'q2'

# Input String
string = input("Enter Input String: ")

current_state = initial_state
path = [current_state]

for symbol in string:
    if (current_state, symbol) in transition:
        current_state = transition[(current_state, symbol)]
        path.append(current_state)
    else:
        print("Invalid Input")
        exit()

print("\nTransition Path:")
print(" → ".join(path))

if current_state == final_state:
    print("Accepted")
else:
    print("Rejected")
