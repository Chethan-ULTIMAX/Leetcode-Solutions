# Problem: Stone Game IX
# LeetCode: 2029
#
# Approach: Counting Remainders
# -----------------------------
# Count how many stones have remainders
# 0, 1, and 2 when divided by 3.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        remainder_one = 0
        remainder_two = 0
        remainder_zero = 0

        for stone in stones:
            if stone % 3 == 0:
                remainder_zero += 1
            elif stone % 3 == 1:
                remainder_one += 1
            else:
                remainder_two += 1

        if remainder_zero % 2 == 0:
            return remainder_one > 0 and remainder_two > 0
        else:
            return abs(remainder_one - remainder_two) > 2
