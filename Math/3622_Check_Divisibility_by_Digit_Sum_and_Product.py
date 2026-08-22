# Problem: Check Divisibility by Digit Sum and Product
# LeetCode: 3622
#
# Approach: Digit Sum and Product
# ------------------------------
# Calculate the sum and product of all digits.
# The number is divisible if it is divisible by
# the sum of its digits plus the product of its digits.
#
# Time Complexity: O(d)
# Space Complexity: O(d)
# where d is the number of digits.

class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """

        digit_sum = 0
        digit_product = 1

        number = str(n)

        for digit in number:
            value = int(digit)
            digit_sum += value
            digit_product *= value

        return n % (digit_sum + digit_product) == 0
