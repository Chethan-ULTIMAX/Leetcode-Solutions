# Problem: Finding 3-Digit Even Numbers
# LeetCode: 2094
#
# Approach: Brute Force + Set
# --------------------------
# Try every possible combination of three different indices.
#
# The first digit cannot be zero because the number must
# have exactly three digits.
#
# The last digit must be even because the number must be even.
#
# A set is used to remove duplicate numbers when the input
# contains repeated digits.
#
# Time Complexity: O(n³)
# Space Complexity: O(n³)

class Solution:
    def totalNumbers(self, digits):
        unique_numbers = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Each digit must come from a different index.
                    if i != j and i != k and j != k:

                        # First digit cannot be zero.
                        if digits[i] != 0:

                            # Last digit must be even.
                            if digits[k] % 2 == 0:
                                number = digits[i] * 100 + digits[j] * 10 + digits[k]
                                unique_numbers.add(number)

        return len(unique_numbers)
