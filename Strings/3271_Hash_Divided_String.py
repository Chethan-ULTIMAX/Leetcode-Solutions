class Solution:
    def stringHash(self, s: str, k: int) -> str:
        summ = 0
        t = 0
        result = []

        for i in range(len(s)):
            summ += ord(s[i]) - ord('a')
            t += 1

            if t == k:
                summ %= 26
                result.append(chr(summ + ord('a')))
                summ = 0
                t = 0

        return ''.join(result)