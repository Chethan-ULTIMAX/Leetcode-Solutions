# Problem: Daily Temperatures
# LeetCode: 739
#
# Approach: Monotonic Stack
# -------------------------
# Store indices of temperatures that are waiting
# for a warmer temperature. When a warmer day is
# found, resolve the previous indices.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                previous = stack.pop()
                answer[previous] = i - previous

            stack.append(i)

        return answer
