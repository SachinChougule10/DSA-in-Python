# Leetocde : 49. Group Anagrams Given an array of strings strs, group the anagrams together. You can return the answer in any order (Frequency-Based Optimal Approach (Most Efficient))

from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        # Dictionary to store grouped anagrams
        # Key   -> tuple representing character frequency
        # Value -> list of anagram strings
        anagrams_dict = defaultdict(list)

        # Iterate through each string in the input list
        for string in strs:
            # Create a frequency array for 26 lowercase letters
            count = [0] * 26

            # Count frequency of each character in the string
            for ch in string:
                # Map character to index (0 for 'a', 1 for 'b', ..., 25 for 'z')
                count[ord(ch) - ord("a")] += 1

            # Convert list to tuple (hashable) and use it as dictionary key
            anagrams_dict[tuple(count)].append(string)

        # Return all grouped anagrams as a list
        return list(anagrams_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

obj = Solution()
print(obj.group_anagrams(strs))
# output : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""
Logic:

1. Two strings are anagrams if they have the same characters with the same frequencies.
2. For each string, we create a frequency array of size 26 (for letters 'a' to 'z').
3. Each index in the array represents the count of a particular character.
4. This frequency array is converted to a tuple so it can be used as a dictionary key.
5. All strings with identical frequency tuples are grouped together.
6. Finally, we return all values from the dictionary as the result.

TIME COMPLEXITY:
- O(n * k), where:
  n = number of strings
  k = average length of each string

SPACE COMPLEXITY:
- O(n), for storing the grouped anagrams
"""
