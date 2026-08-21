# Problem: K-th Smallest Amount With Single Denomination Combination
# LeetCode: 3116
#
# Approach: Binary Search + Inclusion-Exclusion
# ---------------------------------------------
# count(x) calculates how many positive integers <= x
# are divisible by at least one coin.
#
# Inclusion-exclusion is used to avoid counting
# numbers divisible by multiple coins more than once.
#
# Binary search finds the smallest value x for which
# at least k valid amounts exist.
#
# Time Complexity: O(2^n * n * log(k * min(coins)))
# Space Complexity: O(1)

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
