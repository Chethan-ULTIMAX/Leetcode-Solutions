// Problem: Subtract the Product and Sum of Digits of an Integer
// LeetCode: 1281
//
// Approach: Digit Extraction
// --------------------------
// Extract each digit using n % 10.
// Add the digit to sum and multiply it into mul.
//
// Finally, return:
// product of digits - sum of digits
//
// Time Complexity: O(log n)
// Space Complexity: O(1)

class Solution {
    public int subtractProductAndSum(int n) {
        int sum = 0;
        int mul = 1;

        while (n > 0) {
            int digit = n % 10;

            sum += digit;
            mul *= digit;

            n /= 10;
        }

        return mul - sum;
    }
}
