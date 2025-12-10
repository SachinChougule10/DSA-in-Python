class Solution:
    def bestTimetoSellandBuy(self, prices: list[int]) -> int:

        n = len(prices)
        max_profit = 0
        min_price = prices[0]
        # Initialize with the first price as the current minimum

        for price in prices:
            min_price = min(min_price, price)
            # Update lowest price seen so far (best day to buy)
            max_profit = max(max_profit, price - min_price)
            # Profit if sold today; update max if better
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
obj = Solution()
print(obj.bestTimetoSellandBuy(prices))


# Time Complexity: O(n)
# Space Complexity: O(1)

# Logic:
# - The best time to buy a stock must always be before we sell it.
# - Instead of checking all pairs (O(n²)), we maintain:
#       min_price   → the lowest price seen so far (best buying point)
#       max_profit  → the highest profit achievable so far
# - For each day:
#       a) Update min_price if we find a new lower price.
#       b) Calculate today's profit = price - min_price.
#       c) Update max_profit if today's profit is greater.
# - This single-pass logic ensures O(n) time and O(1) space.
