# Problem: Valid Parentheses
# LeetCode: 20
#
# Approach: Stack
# -------------
# Push opening brackets onto the stack.
# For every closing bracket, check whether
# it matches the most recent opening bracket.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:

            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

            else:
                stack.append(char)

        return not stack
