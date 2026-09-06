class Solution(object):
    def countGoodRotations(self, nums):
        n = len(nums)
        h = n // 2
        total = sum(nums)
        peldarquin = nums
        half = sum(nums[:h])
        ans = 0
        for i in range(n):
            if half > total - half:
                ans += 1
            half -= nums[i]
            half += nums[(i + h) % n]
        return ans