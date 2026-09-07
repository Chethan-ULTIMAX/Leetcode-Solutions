# Problem: Distinct Subsequences II
# LeetCode: 940
#
# Approach: Dynamic Programming
# ----------------------------
# dp stores the number of distinct subsequences including
# the empty subsequence.
#
# For each character, every existing subsequence can either
# include or exclude the current character, so the count
# initially doubles.
#
# To avoid counting duplicate subsequences, we subtract
# the number of subsequences that were already generated
# when the same character appeared previously.
#
# last[i] stores the value of dp before the previous occurrence
# of character i.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007

        dp = 1
        last = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')

            old_dp = dp

            # Double the subsequences and remove duplicates.
            dp = (2 * dp - last[index] + MOD) % MOD

            # Store the previous dp value for this character.
            last[index] = old_dp

        # Remove the empty subsequence.
        return (dp - 1 + MOD) % MOD
