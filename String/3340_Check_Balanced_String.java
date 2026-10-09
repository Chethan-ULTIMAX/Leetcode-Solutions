// Problem: Check Balanced String
// LeetCode #3340
// Approach: Add digits at even indices and odd indices separately, then compare the sums.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public boolean isBalanced(String num) {
        int evenSum = 0;
        int oddSum = 0;

        for (int i = 0; i < num.length(); i++) {
            int digit = num.charAt(i) - '0'; // Convert char to int
            if (i % 2 == 0) {
                evenSum += digit;
            } else {
                oddSum += digit;
            }
        }
        return evenSum == oddSum;
    }
}
