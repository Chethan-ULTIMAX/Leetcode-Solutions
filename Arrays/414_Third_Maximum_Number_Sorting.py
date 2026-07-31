# Problem: Third Maximum Number
# LeetCode: 414
#
# Approach: Sorting + Hash Set
# ----------------------------
# Remove duplicate values using a set,
# sort the unique elements, and return
# the third maximum if it exists.
# Otherwise, return the maximum element.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_nums = sorted(set(nums))

        if len(unique_nums) >= 3:
            return unique_nums[-3]

        return unique_nums[-1]
