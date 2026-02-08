# Leetocde : 49. Group Anagrams Given an array of strings strs, group the anagrams together. You can return the answer in any order (Sorting-Based Optimal Approach)

from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        # Dictionary to store sorted string as key and list of anagrams as value
        anagrams_dict = defaultdict(list)

        # Iterate through each string
        for string in strs:
            # Anagrams have identical sorted strings, so we use it as the key
            key = "".join(sorted(string))
            # Append the original string to the corresponding anagram group
            anagrams_dict[key].append(string)
        # Return all grouped anagrams
        return list(anagrams_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

obj = Solution()
print(obj.group_anagrams(strs))
# output : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""
Logic:

1. Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.

2. For each string, we sort its characters.
   All anagrams produce the same sorted string.

3. The sorted string is used as a key in a dictionary.
   Strings with the same key belong to the same anagram group.

4. A dictionary is used to collect all strings that share the same sorted key.

5. Finally, all grouped values from the dictionary are returned as the result.

Time Complexity:
- O(n * k log k)
  where n is the number of strings and
  k is the average length of each string.

Space Complexity:
- O(n), used for storing grouped anagrams.
"""
