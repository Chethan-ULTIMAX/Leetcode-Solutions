// Problem: Smallest Index With Digit Sum Equal to Index
// LeetCode: 3550
//
// Approach: Digit Sum
// -------------------
// For every index, calculate the sum of the digits of nums[i].
// If the digit sum equals the current index, return that index.
//
// Since we scan from left to right, the first matching index
// is automatically the smallest one.
//
// Time Complexity: O(n * d)
// Space Complexity: O(1)
//
// n = number of elements
// d = number of digits in nums[i]

class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;

            // Calculate the digit sum.
            for (int t = nums[i]; t > 0; t /= 10) {
                sum += t % 10;
            }

            if (sum == i) {
                return i;
            }
        }

        return -1;
    }
}
