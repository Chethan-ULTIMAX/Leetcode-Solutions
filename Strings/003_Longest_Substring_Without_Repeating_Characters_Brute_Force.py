# Problem: Longest Substring Without Repeating Characters
# LeetCode: 3
#
# Approach: Brute Force
# ---------------------
# Start from each character and build a substring
# until a repeated character is found.
# Keep track of the longest substring encountered.
#
# Time Complexity: O(n²)
# Space Complexity: O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        longest = ""

        for i in range(n):
            current = s[i]

            for j in range(i + 1, n):
                if s[j] in current:
                    break

                current += s[j]

            if len(current) > len(longest):
                longest = current

        return len(longest)
