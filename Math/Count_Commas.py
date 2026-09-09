# Problem: Count Commas
#
# Approach: Mathematical Observation
# -----------------------------------
# A comma appears in every number starting from 1,000.
# For each comma position (thousands, millions, billions, ...),
# count how many numbers up to n reach that position.
#
# base represents the smallest number that needs a comma
# at the current position.
#
# For each base:
#   n - base + 1
# numbers contain that comma.
#
# Time Complexity: O(log₁₀(n))
# Space Complexity: O(1)

class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        base = 1000

        while n >= base:
            total_commas += n - base + 1
            base *= 1000

        return total_commas
