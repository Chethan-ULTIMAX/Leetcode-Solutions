class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        s = []
        for i in range(n):
            while s and temperatures[s[-1]] < temperatures[i]:
                a = s.pop()
                ans[a] = i - a
            s.append(i)
        return ans