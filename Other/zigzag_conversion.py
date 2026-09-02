class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :type rtype: str
        """
        if numRows == 1:
            return s
        ans = [[] for i in range(numRows)]
        while s:
            for i in range(numRows):
                if not s:
                    break
                ans[i].append(s[0])
                s = s[1:]
            for j in range(numRows - 2, 0, -1):
                if not s:
                    break
                ans[j].append(s[0])
                s = s[1:]         
        a = ""
        for r in ans:
            for c in r:
                a += c
                
        return a