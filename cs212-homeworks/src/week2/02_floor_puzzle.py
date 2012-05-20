#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    floors = [1, 2, 3, 4, 5]
    floor_orderings = list(itertools.permutations(floors))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in floor_orderings:
        if Hopper is not 5 and Kay is not 1 and Liskov is not 5 and Liskov is not 1 and Perlis > Kay and abs(Ritchie - Liskov) > 1 and abs(Liskov - Kay) > 1:
            return list((Hopper, Kay, Liskov, Perlis, Ritchie))
    return None
    #return next((Hopper, Kay, Liskov, Perlis, Ritchie)
    #            for (Hopper, Kay, Liskov, Perlis, Ritchie) in floor_orderings
    #            if Hopper is not 5
    #            if Kay is not 1 
    #            if Liskov is not 5 
    #            if Liskov is not 1 
    #            if Perlis > Kay
    #            if abs(Ritchie - Liskov) > 1 
    #            if abs(Liskov - Kay) > 1
    #            )

print floor_puzzle()