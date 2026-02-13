# GFG: Problem Summary: Given a string, sort its characters based on their frequency.
# If two characters have the same frequency, sort them lexicographically (alphabetical order).


class Solution:
    def sort_by_frequency(self, s: str) -> str:
        # Dictionary to store character frequencies
        hash_map = {}
        # Final result string
        result = ""

        # Step 1: Count frequency of each character
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        # Step 2: Sort characters by frequency and then lexicographically
        # x[0] -> character
        # x[1] -> frequency
        sorted_chars = sorted(hash_map.items(), key=lambda x: (x[1], x[0]))

        # Step 3: Build the result string
        for key, freq in sorted_chars:
            result += key * freq  # Repeat character 'freq' times

        return result


obj = Solution()

s1 = "tree"
print(obj.sort_by_frequency(s1))  # output : rtee

s2 = "cccaaa"
print(obj.sort_by_frequency(s2))  # output : aaaccc


"""
Logic:

1. We first create an empty dictionary (hash_map) to store the frequency of each character in the string.

2. We iterate through the string:
       hash_map[ch] = hash_map.get(ch, 0) + 1
   This counts how many times each character appears.

3. We then sort the dictionary items using:
       sorted(hash_map.items(), key=lambda x: (x[1], x[0]))

   Here:
       x[0] -> character
       x[1] -> frequency

   Sorting logic:
       - First by frequency
       - Then by character (lexicographical order) as tie-breaker

4. After sorting, we build the final result string by:
       result += key * freq
   This repeats each character according to its frequency.

5. Finally, we return the constructed result string.

Time Complexity:
    O(n log k)
    - n = length of string
    - k = number of unique characters

Space Complexity:
    O(k)
    - For storing character frequencies
"""
