# LeetCode : 461. Hamming Distance(Brute Force Solution)
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

# Example 1:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:
# Input: x = 3, y = 1
# Output: 1

# Constraints:
# 0 <= x, y <= 231 - 1


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        # Loop until both numbers become 0
        while x > 0 or y > 0:
            # Get last bit of x and y
            bit_x = x % 2
            bit_y = y % 2

            # If bits are different, increase count
            if bit_x != bit_y:
                count += 1

            # Remove last bit (right shift)
            x //= 2
            y //= 2

        return count


obj = Solution()

x1 = 1
y1 = 4
print(obj.hamming_distance(x1, y1))  # Output : 2

x2 = 3
y2 = 1
print(obj.hamming_distance(x2, y2))  # Output : 1

"""
Logic:

1. Start with two integers x and y.

2. Initialize count = 0.

3. Compare bits from right to left:

4. While x > 0 or y > 0:
   
   a. Extract last bits:
        - x % 2 (last bit of x)
        - y % 2 (last bit of y)

   b. If bits differ:
        - Increment count

   c. Remove last bit:
        - x = x // 2
        - y = y // 2

5. Repeat until both become 0.

6. Return count.

Time Complexity:
- O(n), where n = number of bits in the larger number

Space Complexity:
- O(1), constant extra space
"""
