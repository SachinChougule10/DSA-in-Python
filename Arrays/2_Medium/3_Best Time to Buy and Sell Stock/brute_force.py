# Leetcode: 121. Best Time to Buy and Sell Stock :- You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution:
    def bestTimetoSellandBuy(self, nums: list[int]) -> int:
        n = len(nums)
        max_profit = 0  # stores the maximum profit found
        current_profit = 0  # profit for each buy–sell pair

        for i in range(0, n):  # choose a day to buy
            for j in range(i + 1, n):  # choose a later day to sell
                current_profit = nums[j] - nums[i]  # profit of current transaction
                max_profit = max(max_profit, current_profit)  # update max profit
        return max_profit


nums = [7, 2, 1, 5, 6, 4, 8]
obj = Solution()
print(obj.bestTimetoSellandBuy(nums))

# Logic:
# We try every possible pair (i, j) where i < j.
# For each pair, we calculate profit = prices[j] - prices[i].
# We keep updating the maximum profit found.
# This is a brute-force approach because we check all pairs.

# Time Complexity: O(n²) — nested loops check all pairs.
# Space Complexity: O(1) — no extra space used.
