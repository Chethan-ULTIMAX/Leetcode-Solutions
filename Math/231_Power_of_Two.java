// Problem: Power of Two
// LeetCode: 231
//
// Approach: Brute Force
// ---------------------
// Check every power of two from 2^0 through 2^30.
// If any value matches n, return true.
// Otherwise, return false.
//
// Time Complexity: O(1)
// Space Complexity: O(1)

class Solution {
    public boolean isPowerOfTwo(int n) {
        for (int i = 0; i < 31; i++) {
            int ans = (int) Math.pow(2, i);
            if (ans == n) {
                return true;
            }
        }
        return false;
    }
}
