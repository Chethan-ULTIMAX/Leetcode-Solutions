# Problem: Palindrome Number
# LeetCode: 9
#
# Approach: Reverse Integer
# -------------------------
# Negative numbers cannot be palindromes.
# Reverse the digits of the number and compare
# the reversed number with the original.
#
# Time Complexity: O(log₁₀(n))
# Space Complexity: O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return reverse == original
