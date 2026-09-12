# Problem: Longest Valid Parentheses
# LeetCode: 32
#
# Approach: Stack
# ----------------
# Use a stack to store indices of unmatched parentheses.
# Start with -1 as a base index.
#
# When we find '(' , store its index.
# When we find ')' , remove the matching '(' index.
#
# If the stack becomes empty, the current ')' becomes the
# new base index because no valid substring can start before it.
#
# Otherwise, the current valid length is:
# current index - index at the top of the stack.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
