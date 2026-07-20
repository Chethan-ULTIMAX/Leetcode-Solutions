# Problem: Shift 2D Grid
# LeetCode: 1260
#
# Approach: Simulation
# --------------------
# Simulate one shift operation at a time.
# Store the last element, then move every
# element one position forward by traversing
# the grid in reverse order.
#
# Time Complexity: O(k × m × n)
# Space Complexity: O(1)

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        rows = len(grid)
        cols = len(grid[0])

        for _ in range(k):
            last = grid[rows - 1][cols - 1]

            for i in range(rows - 1, -1, -1):
                for j in range(cols - 1, -1, -1):

                    if i == 0 and j == 0:
                        grid[0][0] = last

                    elif j == 0:
                        grid[i][j] = grid[i - 1][cols - 1]

                    else:
                        grid[i][j] = grid[i][j - 1]

        return grid
