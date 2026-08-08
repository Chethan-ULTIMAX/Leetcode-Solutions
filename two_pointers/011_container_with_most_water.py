class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        ans = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            ans = max(ans, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans
