# Problem: Multiply Strings
# LeetCode: 43
#
# Approach: Integer Conversion
# ----------------------------
# Convert both input strings to integers,
# multiply them, and convert the result
# back to a string.
#
# Note:
# This solution uses Python's built-in integer
# conversion. The original LeetCode challenge
# asks you to solve the problem without using
# direct integer conversion.
#
# Time Complexity: O(n + m)
# Space Complexity: O(1)
# (Ignoring the space used by Python's integer representation.)

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        product = int(num1) * int(num2)

        return str(product)
