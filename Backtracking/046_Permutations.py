# Problem: Permutations
# LeetCode: 46
#
# Approach: Backtracking
# ----------------------
# Build the permutation one element at a time.
# The `used` array keeps track of which elements
# have already been selected.
#
# When the current permutation reaches the length
# of nums, add a copy to the answer.
#
# Time Complexity: O(n × n!)
# Space Complexity: O(n)
# (Excluding the space required for the output.)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():

            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                current.append(nums[i])
                used[i] = True

                backtrack()

                current.pop()
                used[i] = False

        backtrack()

        return result
