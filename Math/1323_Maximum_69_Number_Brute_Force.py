# Problem: Maximum 69 Number
# LeetCode: 1323
#
# Approach: Brute Force
# ---------------------
# Try changing each digit once, generate all
# possible numbers, and return the maximum.
#
# Time Complexity: O(n²)
# Space Complexity: O(n²)

class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """

        number = str(num)

        if "6" not in number:
            return num

        candidates = []

        for i in range(len(number)):

            current = ""

            for j in range(len(number)):
                if i == j:
                    if number[j] == "6":
                        current += "9"
                    else:
                        current += "6"
                else:
                    current += number[j]

            candidates.append(int(current))

        return max(candidates)
