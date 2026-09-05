# Problem: Total Waviness of Numbers in Range
# LeetCode: 3640
#
# Approach: Digit Comparison
# --------------------------
# A digit is considered a peak or valley when it is
# either greater than both of its neighboring digits
# or smaller than both of them.
#
# We check every middle digit of each number and count
# how many times this condition occurs.
#
# Time Complexity: O((num2 - num1 + 1) * d)
# Space Complexity: O(d)
#
# where d is the number of digits in a number.

class Solution:
    def waviness(self, x: int) -> int:
        s = str(x)
        cnt = 0

        # Check every digit except the first and last.
        for i in range(1, len(s) - 1):
            if ((s[i] > s[i - 1] and s[i] > s[i + 1]) or
                (s[i] < s[i - 1] and s[i] < s[i + 1])):
                cnt += 1

        return cnt

    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        # Calculate waviness for every number in the range.
        for x in range(num1, num2 + 1):
            ans += self.waviness(x)

        return ans
