# Problem: Maximum Product of Two Largest Digits
#
# Approach: Sorting
# -----------------
# Convert the number into its digits, sort them,
# and multiply the two largest digits.
#
# Time Complexity: O(d log d)
# Space Complexity: O(d)
# where d is the number of digits.

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """

        digits = [int(digit) for digit in str(n)]
        digits.sort()

        return digits[-1] * digits[-2]
