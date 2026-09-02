class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        current = []
        used = [False] * len(nums)

        def backtrack():

            if len(current) == len(nums):
                ans.append(current[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                current.append(nums[i])
                used[i] = True

                backtrack()

                current.pop()
                used[i] = False

        backtrack()

        return ans