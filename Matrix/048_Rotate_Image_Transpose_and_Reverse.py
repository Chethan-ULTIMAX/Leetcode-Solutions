# Problem: Rotate Image
# LeetCode: 48
#
# Approach: Transpose and Reverse
# -------------------------------
# Collect each column of the matrix,
# reverse it, and replace the corresponding
# row to achieve a 90-degree clockwise rotation.
#
# Time Complexity: O(n²)
# Space Complexity: O(n²)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """

        n = len(matrix)
        columns = []

        for col in range(n):
            current_column = []

            for row in matrix:
                current_column.append(row[col])

            columns.append(current_column)

        for row in range(n):
            matrix[row] = columns[row][::-1]
