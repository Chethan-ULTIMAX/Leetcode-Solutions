// Problem: Count Monobit Integers
// LeetCode: 3827
//
// Approach: Bit Manipulation
// --------------------------
// Start the count at 1 to include zero.
// Generate numbers whose binary representation contains
// only 1s: 1, 3, 7, 15, ...
//
// The update (i << 1) | 1 generates the next such number.
// Count each value that does not exceed n.
//
// Time Complexity: O(log n)
// Space Complexity: O(1)

class Solution {
    public int countMonobit(int n) {
        int c = 1;

        for (int i = 1; i <= n; i = (i << 1) | 1) {
            c++;
        }

        return c;
    }
}
