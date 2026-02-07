# Leetocde : 49. Group Anagrams Given an array of strings strs, group the anagrams together. You can return the answer in any order (Brute Force Approach)


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        # This list will store all anagram groups
        result = []

        # Iterate through each string in the input list
        for string in strs:
            # Flag to track whether the string was placed in any group
            placed = False
            # Sort the current string to compare anagram patterns
            sorted_string = sorted(string)

            # Check the current string against each existing group
            for group in result:
                # Compare with the first string of the group
                if sorted_string == sorted(group[0]):
                    # If anagram, add to the existing group
                    group.append(string)
                    placed = True
                    break  # No need to check further groups

            # If string does not match any group, create a new group
            if not placed:
                result.append([string])

        # Return all grouped anagrams
        return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
print(obj.group_anagrams(strs))
# output : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""
Logic (Brute Force Approach):

1. The goal is to group strings that are anagrams of each other.

2. We maintain a list of groups, where each group contains
   strings that are anagrams.

3. For each string in the input list:
   - We try to place it into an existing group.
   - To check if two strings are anagrams, we sort both strings
     and compare their sorted versions.

4. If the string matches the first element of any group, it is added to that group.

5. If the string does not match any existing group, a new group is created.

TIME COMPLEXITY:
- O(n² * k log k)
  where n is the number of strings and
  k is the average length of each string.

SPACE COMPLEXITY:
- O(n), used for storing grouped anagrams.
"""
