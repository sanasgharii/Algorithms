def nim_winning(state: int) -> bool:
    if state == 0:
        #game ended, the opponent just took the last chip
        return False
    else:
        #game not ended yet, there are still chips
        for num_chips in list(range(1,3)): #consider 1 or 2 chips
            copy_state = state
            copy_state -= num_chips # do move
            
            if not nim_winning (copy_state):
                return True
        return False
    


print("Winning position?", nim_winning(3))