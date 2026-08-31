# Problem: Maximum Distinct Characters
# LeetCode: 3760
#
# Approach: Set
# ------------
# A set stores only unique characters.
# Therefore, the length of the set gives
# the number of distinct characters.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(set(s))
