n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 32]

for i in m:
    total = 0
    for j in n:
        if i == j:
            total += 1

    if total == 1:
        occurence = "time"
    else:
        occurence = "times"
    print(f"{i} occurs {total} {occurence}.")

    """
        constraints :-
            1) 1 <= n[i] <= 10
            2) n can have 10⁸ elements
            3) m can have 10⁸ elements
            
    """

    """
        But here, in worst case 'm' and 'n' both can have 10⁸ elements respectively.
        So, in worst case, there will be 10⁸ x 10⁸ = 10¹⁶ operations and  time complexity will become 10¹⁶, which will throw TLE error
    
    """
