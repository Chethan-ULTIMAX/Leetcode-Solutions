# Problem: Smallest Number With All Bits Set
# LeetCode: 3370
#
# Approach: Bit Manipulation
# --------------------------
# A number with all bits set to 1 has the form:
# 1, 3, 7, 15, 31, ...
#
# For such numbers, x & (x + 1) is always 0.
# Starting from n, increment x until this condition
# becomes true.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n

        while (x & (x + 1)) != 0:
            x += 1

        return x
