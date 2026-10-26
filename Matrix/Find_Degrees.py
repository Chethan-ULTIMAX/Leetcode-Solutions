class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(matrix)):
            arr.append(sum(matrix[i]))
        return arr
