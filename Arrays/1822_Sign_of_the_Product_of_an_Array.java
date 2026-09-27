// Problem: Sign of the Product of an Array
// LeetCode: 1822
//
// Approach: Negative Count
// ------------------------
// Count the number of negative elements in the array.
// If any element is zero, return 0 immediately.
//
// If the number of negative elements is odd, the product
// is negative, so return -1.
// Otherwise, return 1.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int arraySign(int[] nums) {
        int ncount = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 0) {
                ncount++;
            } else if (nums[i] == 0) {
                return 0;
            }
        }

        if (ncount % 2 != 0) {
            return -1;
        }

        return 1;
    }
}
