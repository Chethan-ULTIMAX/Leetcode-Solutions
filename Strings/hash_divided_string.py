class Solution:
    def stringHash(self, s: str, k: int) -> str:
        check = 97
        result, t = "", 0
        summ = 0
        for i in range(len(s)):
            summ += ord(s[i]) - 97
            t += 1
            if t == k:
                summ = summ % 26
                result += chr(summ + 97)
                summ, t = 0, 0
        return result