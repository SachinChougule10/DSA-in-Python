class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)  # Length of the input array
        result = set()  # Stores unique triplets (as tuples)

        # Fix the first element one by one
        for i in range(n):
            my_set = set()  # Tracks elements seen so far for this i
            # Fix the second element
            for j in range(i + 1, n):
                # Calculate the required third element
                third = -(nums[i] + nums[j])
                # If third element exists in set, we found a valid triplet
                if third in my_set:
                    temp = [nums[i], nums[j], third]
                    # Sort to avoid duplicate triplets in different orders
                    temp.sort()
                    # Store as tuple (hashable) in result set
                    result.add(tuple(temp))
                # Add current nums[j] to set for future checks
                my_set.add(nums[j])

        # Convert set of tuples to list of lists
        return [list(i) for i in result]


nums = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.three_sum(nums))

"""
1. We fix one element nums[i] using the outer loop.

2. For each fixed nums[i], we reduce the problem to:
    "Find two numbers in the remaining array whose sum is -nums[i]"

3. We use a hash set (my_set) to keep track of elements seen so far while iterating with index j.

4. For every nums[j], we compute:
      third = -(nums[i] + nums[j])

   - If 'third' is already present in my_set, it means:
     nums[i] + nums[j] + third == 0

5. We sort the triplet before inserting it into the result set.
   This ensures that duplicate triplets like [-1, 0, 1] and [1, -1, 0] are treated as the same.

6. The result is stored in a set to automatically avoid duplicates.

7. Finally, we convert the set of tuples into a list of lists and return it.

Data Structures Used:
        1. Hash Set (my_set):
           - Used to store elements already seen for a fixed index i.
           - Enables O(1) average-time lookup to check whether the
             required third element exists.
           - Reset for every new value of i.

        2. Hash Set (result):
           - Stores unique triplets as tuples.
           - Automatically removes duplicate triplets.
           - Tuples are used because lists are not hashable.

Time Complexity:
- O(n²), since we use two nested loops and O(1) average lookup using a set
        - The outer loop runs n times to fix the first element.
        - The inner loop also runs up to n times to fix the second element.
        - Hash set lookup and insertion operations take O(1) average time.
        - Sorting each triplet takes O(1) time since the size is fixed (3 elements).
        - Therefore, the overall time complexity is O(n × n) = O(n²).

Space Complexity:
- O(n) for the hash set used in each iteration
        - The hash set `my_set` can store up to n elements in the worst case for a single iteration of the outer loop.
        - This space is reused for each iteration and does not grow further.
        - Hence, the auxiliary space complexity remains O(n).
        
        Note:
        Space used to store the final output (`result`) depends on the number of valid triplets and is typically excluded from auxiliary space analysis.

This approach is significantly better than the brute-force O(n³) solution and is a common intermediate optimization before the two-pointer method.
"""
