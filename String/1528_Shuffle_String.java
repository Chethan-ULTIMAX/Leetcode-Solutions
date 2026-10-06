// Problem: Shuffle String
// LeetCode #1528
// Approach: Place each character at the position specified by its corresponding index.
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
    public String restoreString(String s, int[] indices) {
        char[] res = new char[s.length()];
        int i = 0;
        for (int n : indices) {
            res[n] = s.charAt(i++);
        }
        return new String(res);
    }
}
