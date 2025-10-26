class Solution:
    def fib(self, n: int) -> int:

        n1, n2 = 0, 1
        if n <= 1:
            return n
        elif n > 2:
            for i in range(1, n):
                n1, n2 = n2, n1 + n2
        return n2


print(Solution().fib(2))


# Space Complexity = The amount of memory used at a time during execution.

# In recursion, this usually refers to the recursion call stack — the memory used to keep track of function calls that haven’t returned yet.
