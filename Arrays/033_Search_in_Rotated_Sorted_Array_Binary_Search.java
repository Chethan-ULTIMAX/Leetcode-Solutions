/*
 * Problem: Search in Rotated Sorted Array
 * LeetCode: 33
 *
 * Approach: Modified Binary Search
 * --------------------------------
 * At every step, one half of the rotated array
 * is guaranteed to be sorted. Determine which half
 * is sorted and check whether the target lies in it.
 *
 * Time Complexity: O(log n)
 * Space Complexity: O(1)
 */

class Solution {

    public int search(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {

            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Left half is sorted.
            if (nums[left] <= nums[mid]) {

                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }

            } else {

                // Right half is sorted.
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}
