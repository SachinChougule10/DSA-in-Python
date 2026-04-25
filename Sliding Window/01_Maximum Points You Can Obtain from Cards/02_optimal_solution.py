# LeetCode : 1423 :  Maximum Points You Can Obtain from Cards (Optimal Solution)
# There are several cards arranged in a row, and each card has an associated number of points.
# The points are given in the integer array cardPoints.In one step, you can take one card from the beginning or from the end of the row.
# You have to take exactly k cards.Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score.
# The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

# Example 2:
# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always be 4.

# Example 3:
# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points of all cards.


# Constraints:

# 1 <= cardPoints.length <= 105
# 1 <= cardPoints[i] <= 104
# 1 <= k <= cardPoints.length


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:

        n = len(cardPoints)
        lSum = 0  # sum of elements taken from left
        rSum = 0  # sum of elements taken from right
        maxSum = 0  # stores maximum score

        # Step 1: Take first k elements from left
        for i in range(k):
            lSum += cardPoints[i]

        # Initialize maxSum with all k elements from left
        maxSum = lSum

        # pointer to take elements from right
        rightIndex = n - 1

        # Step 2: Try taking some from right and rest from left
        for i in range(k - 1, -1, -1):
            # Remove one element from left side
            lSum -= cardPoints[i]

            # Add one element from right side
            rSum += cardPoints[rightIndex]

            # Move right pointer leftwards
            rightIndex -= 1

            # Current sum = left + right
            currSum = rSum + lSum

            # Update max
            maxSum = max(maxSum, currSum)

        return maxSum


obj = Solution()

cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
print(obj.maxScore(cardPoints1, 3))  # Output : 12

cardPoints2 = [9, 7, 7, 9, 7, 7, 9]
print(obj.maxScore(cardPoints2, 7))  # Output : 55


"""
LOGIC & INTUITION:

We must pick exactly k cards from either:
- left side
- right side

Instead of trying all combinations (which is expensive), we use an observation:

If we take x cards from left, then we must take (k - x) cards from right.

So total possibilities = k + 1 cases:
    (k left, 0 right)
    (k-1 left, 1 right)
    (k-2 left, 2 right)
    ...
    (0 left, k right)

--------------------------------------------------

APPROACH:

1. First, take all k elements from LEFT → initial sum.
2. Then gradually:
   - remove one element from LEFT
   - add one element from RIGHT
   - update max sum

This way, we efficiently check all combinations.

--------------------------------------------------

EXAMPLE:

cardPoints = [1,2,3,4,5,6,1], k = 3

Initial:
Take [1,2,3] → sum = 6

Then:
Remove 3, add 1 → sum = 4
Remove 2, add 6 → sum = 8
Remove 1, add 5 → sum = 12  -> max

--------------------------------------------------

WHY THIS WORKS:

We are effectively sliding a "window" across:
- left part shrinks
- right part grows

This avoids recomputing sums again and again.

--------------------------------------------------

TIME COMPLEXITY:
O(k)

- First loop runs k times
- Second loop runs k times

--------------------------------------------------

SPACE COMPLEXITY:
O(1)

- Only variables used, no extra space

--------------------------------------------------

KEY INSIGHT:

Instead of thinking:
"pick from left or right"

Think:
"how many from left + how many from right"

This transforms problem into a sliding window style solution.
"""
