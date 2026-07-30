/*
 * Problem: Minimum Number of Pushes to Type Word I
 * LeetCode: 3014
 *
 * Approach: Mathematical Observation
 * ----------------------------------
 * The first 8 characters require 1 push each.
 * The next 8 characters require 2 pushes each.
 * The next 8 characters require 3 pushes each.
 * Any remaining characters require 4 pushes each.
 *
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */

class Solution {
    public int minimumPushes(String word) {

        int length = word.length();

        if (length <= 8) {
            return length;
        }

        if (length <= 16) {
            return 8 + (length - 8) * 2;
        }

        if (length <= 24) {
            return 8 + 8 * 2 + (length - 16) * 3;
        }

        return 8 + 8 * 2 + 8 * 3 + (length - 24) * 4;
    }
}
