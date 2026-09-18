// Problem: Score of a String
// LeetCode: 3110
//
// Approach: Adjacent Character Difference
// ----------------------------------------
// Compare every character with the next character.
// Add the absolute difference between their ASCII values.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int scoreOfString(String s) {
        int ans = 0;

        for (int i = 0; i < s.length() - 1; i++) {
            ans += Math.abs(s.charAt(i) - s.charAt(i + 1));
        }

        return ans;
    }
}
