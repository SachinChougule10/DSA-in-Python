# Leetcode : 205. Isomorphic Strings : Given two strings s and t, determine if they are isomorphic (Optimal Solution)
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'
# Mapping 'g' to 'd'


class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        # If lengths are different, strings cannot be isomorphic
        if len(s) != len(t):
            return False

        # Dictionary to store mapping from s -> t
        s_to_t = {}
        # Dictionary to store reverse mapping from t -> s. This ensures no two characters in s map to same character in t
        t_to_s = {}

        # Traverse both strings simultaneously
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # If character from s was seen before verify it maps to the same character in t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # Create new mapping s -> t
                s_to_t[char_s] = char_t

            # Now check reverse mapping
            # If character from t was seen before verify it maps back to same character in s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                # Create reverse mapping t -> s
                t_to_s[char_t] = char_s

        # If no inconsistencies found
        return True


s1, t1 = "paper", "title"
s2, t2 = "badc", "kikp"
s3, t3 = "paperpe", "titlesl"

obj = Solution()
print(obj.is_isomorphic(s1, t1))  # output : True
print(obj.is_isomorphic(s2, t2))  # output : False
print(obj.is_isomorphic(s3, t3))  # output : False


"""
Logic:

Problem Intuition:
Two strings are isomorphic if there exists a one-to-one (bijective) mapping between characters of s and t.

This means:
1) Each character in s must map to exactly one character in t.
2) No two different characters in s can map to the same character in t.
3) Order must be preserved.

------------------------------------------------------------

WHY TWO HASHMAPS?

We maintain:

    s_to_t  → forward mapping
    t_to_s  → reverse mapping

Forward mapping ensures:
    A character in s always maps to the same character in t.

Reverse mapping ensures:
    No two characters in s map to the same character in t.

If we only used one hashmap (s_to_t),
we would miss cases like:

    s = "ab"
    t = "aa"

Forward mapping:
    a → a
    b → a

This looks valid in one direction,
but violates rule that two characters cannot map to same target.

Reverse mapping catches this inconsistency.

------------------------------------------------------------

EXAMPLE WALKTHROUGH:

Example:
    s = "paper"
    t = "title"

Iteration 1:
    p → t
    Store:
        s_to_t = {p: t}
        t_to_s = {t: p}

Iteration 2:
    a → i
    Store:
        s_to_t = {p: t, a: i}
        t_to_s = {t: p, i: a}

Iteration 3:
    p → t
    Already mapped, check consistency → OK

Iteration 4:
    e → l
    Store new mapping

Iteration 5:
    r → e
    Store new mapping

No violations found → return True

-------------------------------------------------------------

TIME COMPLEXITY:
O(n)
We traverse the string once.

SPACE COMPLEXITY:
O(n)
In worst case, all characters are unique.

------------------------------------------------------------
"""
