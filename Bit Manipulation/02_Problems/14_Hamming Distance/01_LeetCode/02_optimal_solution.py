# LeetCode : 461. Hamming Distance(Optimal Solution)
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
    def hamming_distance(self, x: int, y: int) -> int:
        # Step 1: XOR gives 1 where bits are different
        xor = x ^ y

        count = 0

        # Step 2: Loop until xor becomes 0
        while xor:
            # Remove the rightmost set bit
            xor = xor & (xor - 1)

            # Increment count for each removed set bit
            count += 1

        # Step 3: Number of removed set bits = Hamming Distance
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

2. Compute XOR of x and y:
   - xor = x ^ y
   - XOR sets bits to 1 where x and y differ, else 0.
   - So, number of 1s in xor = Hamming Distance.

3. Initialize count = 0.

4. Use Brian Kernighan’s Algorithm to count set bits:
   - While xor != 0:
        a. xor = xor & (xor - 1)
           → Removes the rightmost set bit from xor.
        b. Increment count by 1.

5. Repeat until xor becomes 0.

6. Return count.

Time Complexity:
- O(k), where k = number of set bits in (x ^ y)
- Efficient because it only iterates over set bits

Space Complexity:
- O(1), constant extra space
"""
