# Problem: Maximum Gap
# LeetCode: 164
#
# Approach: Sorting
# ----------------
# Sort the numbers and find the largest difference
# between every pair of adjacent elements.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n <= 1:
            return 0

        numbers = sorted(nums)
        max_gap = 0

        for i in range(n - 1):
            gap = numbers[i + 1] - numbers[i]
            max_gap = max(max_gap, gap)

        return max_gap
