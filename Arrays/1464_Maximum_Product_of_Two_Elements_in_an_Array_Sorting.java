/*
 * Problem: Maximum Product of Two Elements in an Array
 * LeetCode: 1464
 *
 * Approach: Sorting
 * -----------------
 * Sort the array in ascending order.
 * The two largest elements will be at the end
 * of the array. Compute the product after
 * subtracting one from each.
 *
 * Time Complexity: O(n log n)
 * Space Complexity: O(1)
 * (Ignoring the space used by the sorting algorithm.)
 */

import java.util.Arrays;

class Solution {
    public int maxProduct(int[] nums) {

        Arrays.sort(nums);

        int n = nums.length;

        return (nums[n - 1] - 1) * (nums[n - 2] - 1);
    }
}
