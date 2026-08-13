/*
 * Problem: Concatenation of Array
 * LeetCode: 1929
 *
 * Approach: Array Construction
 * ----------------------------
 * Create an array of twice the original length.
 * Copy the original array into both halves.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

class Solution {

    public int[] getConcatenation(int[] nums) {

        int n = nums.length;
        int[] result = new int[n * 2];

        for (int i = 0; i < n; i++) {
            result[i] = nums[i];
            result[i + n] = nums[i];
        }

        return result;
    }
}
