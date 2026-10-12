// Problem: Counting Words With a Given Prefix
// LeetCode #2185
// Approach: Count words that start with the given prefix.
// Time Complexity: O(n * m), where m is the word length checked
// Space Complexity: O(1)

class Solution {
    public int prefixCount(String[] words, String pref) {
        int count = 0;
        for (String word : words) {
            if (word.startsWith(pref)) {
                count++;
            }
        }
        return count;
    }
}
