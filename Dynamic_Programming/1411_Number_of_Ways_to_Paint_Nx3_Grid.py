class Solution:
    def numOfWays(self, n):
        a = 6
        b = 6

        for i in range(1, n):
            x = 3 * a + 2 * b
            y = 2 * a + 2 * b

            a = x
            b = y

        return (a + b) % 1000000007
