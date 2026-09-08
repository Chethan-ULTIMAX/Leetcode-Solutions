# Problem: Count Commas
#
# Approach: Mathematical Observation
# -----------------------------------
# Numbers below 1000 do not contain a comma.
# Starting from 1000, every number contributes one comma
# (for the range covered by this problem).
#
# Therefore, the number of commas is simply:
# n - 999
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """

        # No commas in numbers below 1000.
        if n < 1000:
            return 0

        return n - 999
