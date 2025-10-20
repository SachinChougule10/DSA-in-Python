s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

hash_dict = {}

for char in s:
    if char in hash_dict:
        hash_dict[char] += 1
    else:
        hash_dict[char] = 1

for x in hash_dict:
    print(f"Frequency of {x}: ", hash_dict[x])

    """
        TC = O(m + n)
        SC = O(k)       ... k = no.of unique characters in 's'
        In worst case, if all the characters are unique in 's', then SC = O(n) (n = no.of characters)
    """
