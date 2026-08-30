# Problem: Divide Two Integers
# LeetCode: 29
#
# Approach: Bit Manipulation
# -------------------------
# Repeatedly subtract the largest possible power-of-two
# multiple of the divisor from the dividend.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor:
            return 1

        positive = (dividend < 0) == (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            power = 0

            while dividend > (divisor << (power + 1)):
                power += 1

            quotient += 1 << power
            dividend -= divisor << power

        # Handle the 32-bit signed integer overflow case.
        if quotient == (1 << 31) and positive:
            return (1 << 31) - 1

        return quotient if positive else -quotient
