n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 32]

hash_map = {}

for i in n:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

for j in m:
    if j not in hash_map:
        print(f"Frequency of {j}: 0")
    else:
        print(f"Frequency of {j}: ", hash_map[j])

    """
        - TC = O(m + n)
        - SC = O(k) ... (k = no.of unique elements in n)
          In worst case, if all the elements in 'n' are unique, so all the elements will be added to the dict, then SC = O(n)
          
    """
