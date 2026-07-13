# Problem: String to Integer (atoi)
# LeetCode: 8
#
# Approach: String Traversal
# --------------------------
# Skip leading whitespaces.
# Determine the sign if present.
# Convert consecutive digits into an integer.
# Stop when a non-digit character is encountered.
# Clamp the result within the 32-bit signed integer range.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        sign = 1
        result = 0
        index = 0
        n = len(s)

        # Skip leading spaces
        while index < n and s[index] == " ":
            index += 1

        # Check for sign
        if index < n and (s[index] == "+" or s[index] == "-"):
            if s[index] == "-":
                sign = -1
            index += 1

        # Convert digits
        while index < n and "0" <= s[index] <= "9":
            digit = ord(s[index]) - ord("0")
            result = result * 10 + digit

            if sign == 1 and result > 2**31 - 1:
                return 2**31 - 1

            if sign == -1 and result > 2**31:
                return -2**31

            index += 1

        return sign * result
