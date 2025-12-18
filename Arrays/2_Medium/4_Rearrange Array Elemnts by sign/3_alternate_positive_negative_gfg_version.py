# Alternate Positive Negative
# Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

# Note:
# - Resulting array should start with a positive integer (0 will also be considered as a positive integer).
# - If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
# - The array may or may not have the equal number of positive and negative integers.

# Examples:

# Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
# Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.
# Input: arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# Output: [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
# Explanation : The positive numbers are [5, 2, 4, 7, 1, 8, 0] and the negative integers are [-5,-2,-8]. According to the given conditions we will start from the positive integer 5 and then -5 and so on. After reaching -8 there are no negative elements left, so according to the given rule, we will add the remaining elements (in this case positive elements are remaining) as it in by maintaining the relative order.
# Input: arr[] = [9, 5, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 5, -1, 5, -5, 0, -3, 2]
# Explanation: The positive numbers are [9, 5, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 5 and then -1 and so on.


# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)


class Solution:
    def rearrange(self, arr):
        # Separate positive (including 0) and negative numbers
        positive_numbers = [x for x in arr if x >= 0]
        negative_numbers = [x for x in arr if x < 0]

        result = []

        m = len(positive_numbers)
        n = len(negative_numbers)

        i = j = 0  # pointers for positive and negative lists

        # Add elements alternately: positive first, then negative
        while i < m and j < n:
            result.append(positive_numbers[i])
            result.append(negative_numbers[j])
            i += 1
            j += 1

        # If positives are left, append them as it is
        while i < m:
            result.append(positive_numbers[i])
            i += 1

        # If negatives are left, append them as it is
        while j < n:
            result.append(negative_numbers[j])
            j += 1

        # Copy rearranged result back into original array
        for i in range(0, len(arr)):
            arr[i] = result[i]

        return arr


arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
obj = Solution()
print(obj.rearrange(arr))


"""
Logic:
- Separate the array into positive (including 0) and negative numbers
  while maintaining their relative order.
- Use two pointers to alternately insert positive and negative numbers
  into the result array, starting with a positive number.
- If one type of number gets exhausted, append the remaining elements
  of the other type as it is.
- Finally, copy the result back into the original array.

Time Complexity: O(n)
- One pass to separate elements and one pass to rebuild the array.

Space Complexity: O(n)
- Extra space used for positive, negative, and result arrays.
"""
