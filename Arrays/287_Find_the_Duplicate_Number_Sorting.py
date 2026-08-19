# Problem: Find the Duplicate Number
# LeetCode: 287
#
# Approach: Sorting
# ----------------
# Sort the array and check adjacent elements.
# The first pair of equal elements is the duplicate.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# (Ignoring the sorting implementation's internal space.)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
