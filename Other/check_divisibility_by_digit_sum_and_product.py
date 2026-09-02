class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        p = 1
        n = str(n)
        for i in n:
            s += int(i)
            p *= int(i)
        return int(n) % (s+p) == 0