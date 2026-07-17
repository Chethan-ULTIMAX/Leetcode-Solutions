# Problem: Spiral Matrix
# LeetCode: 54
#
# Approach: Boundary Traversal
# ----------------------------
# Maintain four boundaries:
#   - top
#   - bottom
#   - left
#   - right
#
# Traverse the matrix layer by layer:
# 1. Left to Right
# 2. Top to Bottom
# 3. Right to Left
# 4. Bottom to Top
#
# Update the boundaries after each traversal
# until all elements are visited.
#
# Time Complexity: O(m × n)
# Space Complexity: O(1)
# (Excluding the output array.)

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        result = []

        while left <= right and top <= bottom:

            # Traverse left to right
            result.extend(matrix[top][left:right + 1])
            top += 1

            # Traverse top to bottom
            if top <= bottom:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1

            # Traverse right to left
            if left <= right:
                result.extend(matrix[bottom][left:right + 1][::-1])
                bottom -= 1

            # Traverse bottom to top
            if top <= bottom:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
