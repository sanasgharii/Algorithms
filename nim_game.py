def nim_winning(state: int) -> bool:
    if state == 0:
        #game ended, the opponent just took the last chip
        print("no cards left")
        return False
        
    else:
        #game not ended yet, there are still chips
        for num_chips in list(range(1,3)): #consider 1 or 2 chips
            copy_state = state
            print("copy_state is " ,  copy_state )
            current_state = copy_state - num_chips # do move
            print("current state is ", current_state)
            
            
            if not nim_winning (current_state):
                print("winning state")
                return True
        print("false1")
        return False
    


print("Winning position?", nim_winning(4))