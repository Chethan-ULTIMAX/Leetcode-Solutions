# Problem: Reverse Degree of a String
# LeetCode: 3498
#
# Approach: Character Value + Position
# -------------------------------------
# Calculate the reverse alphabetical value of each character:
# a = 26, b = 25, ..., z = 1.
#
# Multiply each value by its 1-based position and add
# everything to get the reverse degree.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            # Calculate reverse alphabetical value.
            value = 26 - (ord(s[i]) - ord('a'))

            # Multiply by the 1-based position.
            ans += value * (i + 1)

        return ans
