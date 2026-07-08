# Problem: Reverse Integer
# LeetCode: 7
#
# Approach: Digit Extraction
# --------------------------
# Determine the sign of the integer.
# Reverse the number by extracting one digit
# at a time using modulo (%) and integer division (//).
# Finally, check whether the reversed integer
# lies within the 32-bit signed integer range.
#
# Time Complexity: O(log₁₀(n))
# Space Complexity: O(1)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
