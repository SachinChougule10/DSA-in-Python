# Leetcode : 451. Sort Characters By Frequency : Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Approach 1: Hash Map + Sorting by Frequency - Sort characters based only on frequency in descending order (any valid order for ties)

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
        # Create a hash map (dictionary) to store character frequencies
        hash_map = {}
        result = ""

        # Count frequency of each character
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        # Sort the dictionary items based on frequency (value)
        # x[1] refers to frequency
        # reverse=True ensures descending order
        sorted_chars = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

        # For each (character, frequency) pair, multiply character by its frequency and append to result
        for key, freq in sorted_chars:
            result += key * freq

        return result


obj = Solution()

s1 = "tree"
print(obj.sort_by_frequency(s1))  # Output: "eetr"

s2 = "cccaaa"
print(obj.sort_by_frequency(s2))  # Output: "cccaaa"

"""
Logic:

Problem Understanding:
----------------------
We need to sort characters in a string based on their frequency in decreasing order.

If multiple characters have the same frequency, any valid order is acceptable.

Approach:
---------
1) Count Frequencies (Using Hash Map):
   - Traverse the string.
   - Store frequency of each character in a dictionary.
   - Example:
        "tree"
        -> {'t':1, 'r':1, 'e':2}

2) Sort by Frequency:
   - Use sorted() on dictionary items.
   - Sort based on frequency (value).
   - reverse=True ensures descending order.

3) Build Result:
   - For each (character, frequency) pair: repeat the character 'frequency' times.
   - Append to result string.

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
