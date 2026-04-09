# GFG : Single Number
# Given an array arr[] of positive integers where every element appears even times except for one (Brute Force Solution)
# Find that number occurring an odd number of times.

# Examples:
# Input: arr[] = [1, 1, 2, 2, 2]
# Output: 2
# Explanation: In the given array all element appear two times except 2 which appears thrice.

# Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
# Output: 1
# Explanation: In the given array all element appear two times except 1 which appears once.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ arr.size() ≤ 106
# 0 ≤ arri ≤ 105


class Solution:
    def single_number(self, arr: list[int]) -> int:
        # Dictionary to store frequency of each element
        hash_map = {}

        for num in arr:
            # Count frequency of each number
            hash_map[num] = hash_map.get(num, 0) + 1

        for key, value in hash_map.items():
            # Check for element with odd frequency
            if value % 2 == 1:
                # Return the element occurring odd number of times
                return key


arr = [1, 1, 2, 2, 2]

obj = Solution()
print(obj.single_number(arr))  # Output : 2

"""
Logic: Brute Force using HashMap (Frequency Count)

Approach:
- Use a dictionary (hash_map) to count occurrences of each element
- Traverse the array and store frequency of each number
- Traverse the dictionary and find the element whose frequency is odd

Key Observation:
- All elements appear even number of times except one
- The required element will have frequency % 2 == 1

Example:
arr = [1, 1, 2, 2, 2]

Step 1: Build frequency map
{
    1: 2,
    2: 3
}

Step 2: Find odd frequency
- 1 → 2 (even) → ignore
- 2 → 3 (odd) → answer

Final Answer = 2


Why this works:
- We explicitly count occurrences
- Then identify the number appearing odd number of times

Time Complexity:
- O(n) for building hashmap
- O(n) for checking → Overall O(n)

Space Complexity:
- O(n) → for storing hashmap


Note:
- This is NOT optimal for this problem
- Optimal solution uses XOR (O(1) space)
"""
