# Problem: Two Sum
# LeetCode: 1
#
# Approach: Hash Map (Complement)
# --------------------------------
# Store each number and its index in a dictionary.
# For every element, calculate its complement:
#
#     complement = target - current_number
#
# If the complement already exists in the dictionary,
# return the indices. Otherwise, store the current
# number and continue.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
