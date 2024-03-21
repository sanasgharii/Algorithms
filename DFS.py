import numpy as np

visited = set()
FARMER_IDX = 0
WOLF_IDX = 1
GOAT_IDX = 2
CABBAGE_IDX = 3

#recursive depth first search staretgy to solve this problem

def old_world_puzzle(state, step=0, solution=[]):
    
    """
    rules are:
    1- The farmer can take only one of the other three (wolf, goat, or cabbage) across the river at a time.
    2- The wolf cannot be left alone with the goat, and the goat cannot be left alone with the cabbage, 
        without the farmer's supervision.
    --------------------------------------------------------------
    state : 4-tuple consisting of booleans for each entity in this puzzle.
    
    if False, the entity is on the original side of the river,
    if True, the entitiy is on the other side of the river.
    
    Order of the elements in string --> Farmer Wolf Goat Cabbage
    for example: (False, False, True, False) means only the goat is on the other side of the river 
    
    --------------------------------------------------------------
    step : int counting the depth of the solution (only needed for print statements) 
    """
    
    print(f"\nCurrent state at step {step}: {state}")  # Show current state and step
    
    # Check if state is invalid: wolf and goat alone, or goat and cabbage alone without the farmer.
    if (state[WOLF_IDX] == state[GOAT_IDX] and state[FARMER_IDX] != state[GOAT_IDX]) or \
       (state[GOAT_IDX] == state[CABBAGE_IDX] and state[FARMER_IDX] != state[GOAT_IDX]):
        print("Invalid state, backtracking...")
        return False
    
    # Check for repeated states
    if state in visited:
        print("State already visited, backtracking...")
        return False
    
    print(f"Adding state to visited: {state}")
    visited.add(state)
    solution.append(state)  # Append current state to the solution path
    
    # Check for a solution
    if all(state):
        print("\nSolution sequence!")
        for idx, s in enumerate(solution):
            print(f"Step {idx}: {' '.join(['Farmer', 'Wolf', 'Goat', 'Cabbage'][i] for i in range(4) if s[i])} crossed")
        return True
    
    # Possible states to consider based on the puzzle rules
    possibilities = [
        (not state[FARMER_IDX], state[WOLF_IDX], not state[GOAT_IDX], state[CABBAGE_IDX]),  # Move goat
        (not state[FARMER_IDX], not state[WOLF_IDX], state[GOAT_IDX], state[CABBAGE_IDX]),  # Move wolf
        (not state[FARMER_IDX], state[WOLF_IDX], state[GOAT_IDX], not state[CABBAGE_IDX]),  # Move cabbage
        (not state[FARMER_IDX], state[WOLF_IDX], state[GOAT_IDX], state[CABBAGE_IDX])       # Move farmer alone
    ]
    
    for new_state in possibilities:
        print(f"Trying new state from step {step}: {new_state}")
        if old_world_puzzle(new_state, step + 1, solution.copy()):  # Pass a copy of the solution for correct backtracking
            return True
    
    # Backtrack if no valid moves lead to a solution
    print(f"Backtracking from state: {state}")
    solution.pop()
    return False

# Initial state: everyone on the original side
initial_state = (False, False, False, False)

# Start solving the puzzle
if not old_world_puzzle(initial_state):
    print("\nNo solution found.")
