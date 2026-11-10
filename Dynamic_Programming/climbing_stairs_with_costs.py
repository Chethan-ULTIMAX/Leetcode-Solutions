class Solution(object):
    def climbStairs(self, n, costs):
        ans = [float('inf')] * (n + 1)
        ans[0] = 0

        for i in range(1, n + 1):
            for j in range(max(0, i - 3), i):
                ans[i] = min(ans[i], ans[j] + costs[i-1] + (i-j)**2)

        return ans[n]
