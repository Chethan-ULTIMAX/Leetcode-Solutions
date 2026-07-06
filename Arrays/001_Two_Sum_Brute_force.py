# Problem: Two Sum
# LeetCode: 1
#
# Approach 1: Brute Force
# - Check every possible pair of numbers.
# - If their sum equals the target, return their indices.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
