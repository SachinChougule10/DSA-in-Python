# Leetcode : 451. Sort Characters By Frequency : Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Approach 2: Hash Map + Sorting with Tie-Breaker
# - Sort by frequency (descending)
# - If frequency is same, sort characters alphabetically

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.


class Solution:
    def sort_by_frequency(self, s: str) -> str:
        # Step 1: Create a hash map to store character frequencies
        hash_map = {}
        result = ""

        # Count occurrences of each character
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        # Step 2: Sort characters based on:
        # 1) Frequency in descending order (-x[1])
        # 2) Alphabetical order if frequencies are equal (x[0])
        sorted_chars = sorted(hash_map.items(), key=lambda x: (-x[1], x[0]))

        # Append each character repeated by its frequency
        for key, freq in sorted_chars:
            result += key * freq

        return result


obj = Solution()

s1 = "tree"
print(obj.sort_by_frequency(s1))  # output :- eert

s2 = "cccaaa"
print(obj.sort_by_frequency(s2))  # output :- aaaccc

"""
Logic: 

Problem Understanding:
- We need to sort characters in a string based on their frequency in decreasing order.
- If two characters have the same frequency, they must be sorted alphabetically.

Approach:
---------
1) Frequency Counting (Hash Map):
   - Traverse the string.
   - Store frequency of each character in a dictionary.
   - Example:
        "tree"
        -> {'t':1, 'r':1, 'e':2}

2) Custom Sorting:
   - Use sorted() on dictionary items.
   - Sorting key:
        (-frequency, character)

   Explanation:
   - "-frequency" ensures descending order.
   - "character" ensures alphabetical order for ties.

   Example:
        {'t':1, 'r':1, 'e':2}

   After sorting:
        [('e',2), ('r',1), ('t',1)]

3) Build Result:
   - Multiply each character by its frequency.
   - Concatenate to form final string.

Time Complexity:
----------------
O(n log k)

Where:
n = length of string
k = number of unique characters

- Counting frequency: O(n)
- Sorting unique characters: O(k log k)
- Building result: O(n)

Overall: O(n log k)

Space Complexity:
-----------------
O(k)
- For storing frequency map.
"""
