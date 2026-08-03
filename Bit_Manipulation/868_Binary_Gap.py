# Problem: Binary Gap
# LeetCode: 868
#
# Approach: Binary String Traversal
# --------------------------------
# Convert the number to its binary string.
# For each '1', find the next '1' and keep
# track of the maximum distance between them.
#
# Time Complexity: O(n²)
# Space Complexity: O(n)

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """

        binary = bin(n)[2:]
        length = len(binary)
        max_gap = 0

        for i in range(length):
            if binary[i] == "1":

                for j in range(i + 1, length):
                    if binary[j] == "1":
                        max_gap = max(max_gap, j - i)
                        break

        return max_gap
