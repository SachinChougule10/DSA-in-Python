class Solution:
    def fibonacci_recursion(self, n):
        if n == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        return self.fibonacci_recursion(n - 1) + self.fibonacci_recursion(n - 2)


number = int(input("Enter a number: "))
print(Solution().fibonacci_recursion(number))
