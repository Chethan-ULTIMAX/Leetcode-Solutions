// Problem: Count Elements With Maximum Frequency
// LeetCode: 3005
//
// Approach: Frequency Counting
// -----------------------------
// Count the frequency of every number using an array.
// Whenever a new maximum frequency is found, reset the result.
// If another number reaches the same maximum frequency,
// add its frequency to the result.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int maxFrequencyElements(int[] nums) {
        byte[] freq = new byte[101];
        byte max = 0;
        byte res = 0;

        for (int n : nums) {
            byte f = ++freq[n];

            if (f > max) {
                max = f;
                res = f;
            } else if (f == max) {
                res += f;
            }
        }

        return res;
    }
}
