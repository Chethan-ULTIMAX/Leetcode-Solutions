# Problem: Longest Palindromic Substring
# LeetCode: 5
#
# Approach: Expand Around Center
# ------------------------------
# Treat every character as the center of an odd-length
# palindrome and every gap between characters as the
# center of an even-length palindrome.
#
# Time Complexity: O(n²)
# Space Complexity: O(n)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        longest = ""

        def expand(left, right):
            nonlocal longest

            while left >= 0 and right < n:
                substring = s[left:right + 1]

                if substring != substring[::-1]:
                    break

                if len(substring) > len(longest):
                    longest = substring

                left -= 1
                right += 1

        for i in range(n):
            # Odd-length palindrome
            expand(i, i)

            # Even-length palindrome
            expand(i, i + 1)

        return longest
