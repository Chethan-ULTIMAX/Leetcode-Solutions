# Problem: Sort Array By Parity
# LeetCode: 905
#
# Approach: Two Pointers
# ----------------------
# Keep one pointer at the beginning and one at the end.
# Move the left pointer past even numbers and the right
# pointer past odd numbers. When they are misplaced,
# swap them.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1

        while left < right:

            while left < right and nums[left] % 2 == 0:
                left += 1

            while left < right and nums[right] % 2 == 1:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

        return nums
