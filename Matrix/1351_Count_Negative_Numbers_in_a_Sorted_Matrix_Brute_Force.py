# Problem: Count Negative Numbers in a Sorted Matrix
# LeetCode: 1351
#
# Approach: Brute Force
# ---------------------
# Traverse every element in the matrix and
# count how many values are negative.
#
# Time Complexity: O(m × n)
# Space Complexity: O(1)

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        negative_count = 0

        for row in grid:
            for value in row:
                if value < 0:
                    negative_count += 1

        return negative_count
