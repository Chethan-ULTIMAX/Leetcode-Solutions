// Problem: Squares of a Sorted Array
// LeetCode #977
// Approach: Compare absolute values at both ends and fill the result from right to left.
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] res = new int[nums.length];
        int left = 0;
        int right = nums.length - 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            if (Math.abs(nums[left]) > Math.abs(nums[right])) {
                res[i] = nums[left] * nums[left];
                left++;
            } else {
                res[i] = nums[right] * nums[right];
                right--;
            }
        }
        return res;
    }
}
