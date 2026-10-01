# Problem: Average Value of Even Numbers That Are Divisible by Three
# LeetCode #2455
# Approach: Collect numbers divisible by both 2 and 3, then calculate their average.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                arr.append(i)
        n = len(arr)
        ans = 0
        if n != 0:
            ans = (sum(arr)) / n
        return ans
