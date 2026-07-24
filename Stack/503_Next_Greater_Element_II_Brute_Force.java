/*
 * Problem: Next Greater Element II
 * LeetCode: 503
 *
 * Approach: Brute Force (Circular Traversal)
 * -----------------------------------------
 * For each element, traverse the array in a
 * circular manner to find the first greater
 * element. If no greater element exists,
 * return -1.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 */

class Solution {
    public int[] nextGreaterElements(int[] nums) {

        int n = nums.length;
        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {

            int nextGreater = -1;

            for (int j = 1; j < n; j++) {

                int index = (i + j) % n;

                if (nums[index] > nums[i]) {
                    nextGreater = nums[index];
                    break;
                }
            }

            answer[i] = nextGreater;
        }

        return answer;
    }
}
