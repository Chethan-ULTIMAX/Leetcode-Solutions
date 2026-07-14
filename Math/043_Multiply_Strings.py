# Problem: Multiply Strings
# LeetCode: 43
#
# Approach: Manual Multiplication
# -------------------------------
# Simulate the multiplication process taught in school.
# Multiply each digit of the first number with each digit
# of the second number and store the result in an array.
# Finally, convert the array into the resulting string.
#
# Time Complexity: O(m × n)
# Space Complexity: O(m + n)

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                total = product + result[i + j + 1]

                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        answer = ""

        for digit in result:
            if not (answer == "" and digit == 0):
                answer += str(digit)

        return answer
