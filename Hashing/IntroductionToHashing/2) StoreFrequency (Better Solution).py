n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 32]

hash_list = [0] * (len(n) + 1)

for i in n:
    hash_list[i] += 1

for j in m:
    if j < 1 or j > 10:
        print(f"Frequency of {j}: 0")
    else:
        print(f"Frequency of {j}: ", hash_list[j])

    """
    
        constraints :-
            1) 1 <= n[i] <= 10
            2) n can have 10⁸ elements
            3) m can have 10⁸ elements
            
    
        TIME COMPLEXITY :-
        
            - Here the first for loop runs for n times, second for loop runs for m times.
            - So, time complexity = O(n+m) 
                (here, n + m because, when we have for loops seperate from each other i.e. not inside of another, we add both the complexities)
            - In worst case, 'n' can have 10⁸ elements and 'm' can have 10⁸ elements :-
                So, in worst case there will be 10⁸+10⁸ i.e. 2 x 10⁸ operations, which is nearly similar to 10⁸ and will not give TLE error.
                
        SPACE COMPLEXITY :-

            - Space complexity = O(1)
            - No matter how many elements we have in 'n'(according to constraints, numbers only till 10) or 'm' , the size of hash_list will not increase and will remain constant.
            - The values in the list (frequency of each element) can change, but the size of the list will not increase wrt to the input. 

    
        - We should use List when we know the exact no.of elements, so we can create a list of that size. 
          List is not efficient when we don't know the exact no.of elements or we have very large number of elements.
    """
