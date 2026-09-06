# Problem: Common Factors
#
# Approach: Divisibility Check
# ----------------------------
# Check every number from 1 to a.
# If the number divides both a and b,
# it is a common factor.
#
# Time Complexity: O(a)
# Space Complexity: O(1)

class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        count = 0

        # Check every possible factor.
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                count += 1

        return count
