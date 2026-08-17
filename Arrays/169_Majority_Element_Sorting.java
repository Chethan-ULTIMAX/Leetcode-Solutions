/*
 * Problem: Majority Element
 * LeetCode: 169
 *
 * Approach: Sorting
 * -----------------
 * After sorting, the majority element must
 * occupy the middle position of the array.
 *
 * Time Complexity: O(n log n)
 * Space Complexity: O(1)
 */

import java.util.Arrays;

class Solution {
    public int majorityElement(int[] nums) {

        Arrays.sort(nums);

        return nums[nums.length / 2];
    }
}
