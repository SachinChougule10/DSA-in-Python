# Problem: Swap Two Numbers Using Temporary Variable

# Description:
# This program swaps two integer values using a temporary variable.
# It demonstrates a simple and clear approach to exchange values without losing the original data.

# Example:
# Input: num1 = 5, num2 = 6
# Output: num1 = 6, num2 = 5

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def swap_using_temp(self, num1: int, num2: int):

        # Print original values before swapping
        print(f"old num1: {num1}")  # Output : old num1: 5
        print(f"old num2: {num2}")  # Output : old num2: 6

        # Store value of num1 in a temporary variable
        temp = num1

        # Assign value of num2 to num1
        num1 = num2

        # Assign stored value (temp) to num2
        num2 = temp

        # Print swapped values
        print(f"new num1: {num1}")  # Output : new num1: 6
        print(f"new num2: {num2}")  # Output : new num2: 5


obj = Solution()
obj.swap_using_temp(5, 6)

"""
Logic: Swap Using Temporary Variable

Goal:
Swap two numbers without losing their original values.

Steps:
1) Store the value of the first variable (num1) in a temporary variable.
2) Assign the value of the second variable (num2) to the first variable.
3) Assign the stored value (temp) to the second variable.

Example:
num1 = 5, num2 = 6

Step 1: temp = 5
Step 2: num1 = 6
Step 3: num2 = 5

Final Output:
num1 = 6, num2 = 5

Time Complexity: O(1)
Space Complexity: O(1)
"""
