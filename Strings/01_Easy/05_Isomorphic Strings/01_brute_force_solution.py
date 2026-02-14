# Leetcode : 205. Isomorphic Strings : Given two strings s and t, determine if they are isomorphic.
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
        # If lengths differ, they cannot be isomorphic
        if len(s) != len(t):
            return False

        n = len(s)

        # Compare every pair of indices (i, j)
        # We verify that equality relationships in s, match equality relationships in t
        for i in range(n):
            for j in range(i + 1, n):
                # Case 1: If characters are equal in s, they must also be equal in t
                if s[i] == s[j] and t[i] != t[j]:
                    return False
                # Case 2: If characters are different in s, they must also be different in t
                if s[i] != s[j] and t[i] == t[j]:
                    return False
        # If no structural violation found
        return True


s1, t1 = "paper", "title"
s2, t2 = "badc", "kikp"
s3, t3 = "paperpe", "titlesl"

obj = Solution()
print(obj.is_isomorphic(s1, t1))  # output: True
print(obj.is_isomorphic(s2, t2))  # output: False
print(obj.is_isomorphic(s3, t3))  # output: False

"""
Logic:
Poblem Intuition:
Two strings are isomorphic if they follow the same structural pattern.
We are not comparing characters directly. We are comparing how positions relate to each other.

CORE CONDITION WE ENFORCE:

    s[i] == s[j]   ⇔   t[i] == t[j]

This means:
1) If characters at positions i and j are equal in s, then characters at positions i and j must also be equal in t.

2) If characters at positions i and j are equal in t, then characters at positions i and j must also be equal in s.

This is a bi-conditional (if and only if) condition.

-------------------------------------------------------------------

WHY DO WE COMPARE PAIRS (i, j)?

Because equality is a relationship between two positions.
To verify structure, we must compare every pair.

Example (Valid Case):

    s = "paper"
    t = "title"

Index pattern of s:
    p a p e r
    0 1 0 3 4

Index pattern of t:
    t i t l e
    0 1 0 3 4

Equality relationships match → Isomorphic → True

-------------------------------------------------------------------

WHY TWO IF CONDITIONS?

We use:

    if s[i] == s[j] and t[i] != t[j]:
        return False

    if s[i] != s[j] and t[i] == t[j]:
        return False

The first if enforces:
    s[i] == s[j]  →  t[i] == t[j]

The second if enforces:
    t[i] == t[j]  →  s[i] == s[j]

Both directions are necessary.

-------------------------------------------------------------------

WHAT IF WE KEEP ONLY THE FIRST IF?

Suppose we remove the second condition.

Example:

    s = "ab"
    t = "aa"

Compare positions (0,1):

    s[0] != s[1]
    t[0] == t[1]

First condition checks:
    s[i] == s[j] and t[i] != t[j]

But here:
    s[i] != s[j]

So first condition does NOT trigger.

The function would incorrectly return True ❌

But this is invalid because:
    Two different characters in s map to the same character in t.

So first if alone is not enough.

-------------------------------------------------------------------

WHAT IF WE KEEP ONLY THE SECOND IF?

Suppose we remove the first condition.

Example:

    s = "foo"
    t = "bar"

Compare positions (1,2):

    s[1] == s[2]
    t[1] != t[2]

Second condition checks:
    s[i] != s[j] and t[i] == t[j]

But here:
    s[i] == s[j]

So second condition does NOT trigger.

The function would incorrectly return True ❌

But this is invalid because:
    Same character in s maps to different characters in t.

So second if alone is not enough.

-------------------------------------------------------------------

CONCLUSION:

We must enforce both:

    s[i] == s[j]  ⇔  t[i] == t[j]

To guarantee structural consistency.

Removing either condition checks only half of the rule and may produce incorrect results.

-------------------------------------------------------------------

TIME COMPLEXITY:
O(n²) because we compare every pair (i, j).

SPACE COMPLEXITY:
O(1) since no extra data structures are used.
"""
