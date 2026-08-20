# Problem: Zigzag Conversion
# LeetCode: 6
#
# Approach: Simulation
# --------------------
# Place characters row by row while moving
# down and then diagonally upward through
# the rows. Finally, read the rows in order.
#
# Time Complexity: O(n²)
# Space Complexity: O(n)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        while s:

            for row in range(numRows):
                if not s:
                    break

                rows[row].append(s[0])
                s = s[1:]

            for row in range(numRows - 2, 0, -1):
                if not s:
                    break

                rows[row].append(s[0])
                s = s[1:]

        result = ""

        for row in rows:
            for char in row:
                result += char

        return result
