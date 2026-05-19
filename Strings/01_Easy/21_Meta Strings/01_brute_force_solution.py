# GFG : Meta Strings (Brute Force Solution)
# Given two strings s1 and s2 consisting of lowercase english alphabets, check whether these strings are meta strings or not.
# Note: Meta strings are the strings which can be made equal by exactly one swap in any of the strings. Equal string are not considered here as Meta strings.

# Examples:

# Input: s1 = "geeks", s2 = "keegs"
# Output: true
# Explanation: We can swap the 0th and 3rd character of s2 to make it equal to s1.

# Input: s1 = "geeks", s2 = "geeks"
# Output: false
# Explanation: Equal strings are not considered Meta strings.

# Input: s1 = "a", s2 = "b"
# Output: false
# Explanation: Since there is only character, we cannot do any swap.

# Constraints:
# 1 ≤ |s1|, |s2| ≤ 105

# GeeksForGeeks : Meta Strings (Brute Force Solution)


class Solution:
    def meta_strings(self, s1: str, s2: str) -> bool:

        # lengths must be same
        if len(s1) != len(s2):
            return False

        # equal strings are not meta strings
        if s1 == s2:
            return False

        # convert s1 into list for swapping
        arr = list(s1)

        n = len(arr)

        # try every possible swap
        for i in range(n):

            for j in range(i + 1, n):

                # create copy for swapping
                temp = arr[:]

                # swap characters
                temp[i], temp[j] = temp[j], temp[i]

                # convert back into string
                swapped = "".join(temp)

                # check if strings become equal
                if swapped == s2:
                    return True

        # no valid swap found
        return False


# Example Usage
obj = Solution()

print(obj.meta_strings("geeks", "keegs"))  # Output : True
print(obj.meta_strings("geeks", "geeks"))  # Output : False
print(obj.meta_strings("a", "b"))  # Output : False


"""
Logic (Brute Force Approach):
1. First check if lengths are equal.
2. If both strings are already equal,
   return False because equal strings are not meta strings.
3. Try every possible pair swap in s1.
4. After every swap:
   - create new string
   - compare it with s2
5. If any swapped string equals s2,
   return True.
6. Otherwise return False.

Why It Is Brute Force:
- Every possible swap combination is tested.
- New string creation happens repeatedly.

Time Complexity:
O(n^3)

Space Complexity:
O(n)
because copied list/string is created.
"""
