// Problem: Number of 1 Bits
// LeetCode #191
// Approach: Check each of the 32 bits and count the bits set to 1.
// Time Complexity: O(1)
// Space Complexity: O(1)

public class Solution {
    public int hammingWeight(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1) {
                res += 1;
            }
        }
        return res;
    }
}
