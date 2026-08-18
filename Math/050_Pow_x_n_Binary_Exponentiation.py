# Problem: Pow(x, n)
# LeetCode: 50
#
# Approach: Binary Exponentiation
# ------------------------------
# Repeatedly square x and reduce n by half
# whenever n is even. When n is odd, multiply
# the current value into the answer.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        original_n = n
        n = abs(n)
        result = 1

        while n > 0:
            if n % 2 == 0:
                x *= x
                n //= 2
            else:
                result *= x
                n -= 1

        return result if original_n >= 0 else 1 / result
