// Problem: Counting Bits
// LeetCode #338
// Approach: Use the highest power of two not exceeding i and build on a previously computed bit count.
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
    public int[] countBits(int n) {
        int[] dp = new int[n + 1];
        int sub = 1;

        for (int i = 1; i <= n; i++) {
            if (sub * 2 == i) {
                sub = i;
            }

            dp[i] = dp[i - sub] + 1;
        }

        return dp;
    }
}
