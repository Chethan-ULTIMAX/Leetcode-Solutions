class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        return [num for num in nums if num < pivot] + [num for num in nums if num == pivot] + [num for num in nums if num > pivot]
