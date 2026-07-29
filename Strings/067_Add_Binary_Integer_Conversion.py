# Problem: Add Binary
# LeetCode: 67
#
# Approach: Integer Conversion
# ----------------------------
# Convert both binary strings to integers,
# add them, and convert the result back
# to a binary string.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        num_a = int(a, 2)
        num_b = int(b, 2)

        total = num_a + num_b

        return bin(total)[2:]
