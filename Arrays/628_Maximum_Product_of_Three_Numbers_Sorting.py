# Problem: Maximum Product of Three Numbers
# LeetCode: 628
#
# Approach: Sorting
# -----------------
# Sort the array and compare:
# 1. Product of the three largest numbers.
# 2. Product of the two smallest numbers
#    and the largest number.
#
# The second case is important because two
# negative numbers can produce a positive product.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# (Ignoring the space used by the sorting algorithm.)

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        largest_three = nums[-1] * nums[-2] * nums[-3]
        smallest_two_largest = nums[0] * nums[1] * nums[-1]

        return max(largest_three, smallest_two_largest)
