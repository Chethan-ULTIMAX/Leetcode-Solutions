# Problem: Smallest Divisible Digit Product I
# LeetCode: 3345
#
# Approach: Brute Force
# ---------------------
# Starting from n, compute the product of its
# digits. Return the first number whose digit
# product is divisible by t.
#
# Time Complexity: O(k × d)
# Space Complexity: O(d)
# where:
#   k = numbers checked
#   d = number of digits

class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """

        while True:

            product = 1

            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1
