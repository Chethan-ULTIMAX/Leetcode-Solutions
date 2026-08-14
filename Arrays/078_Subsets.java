/*
 * Problem: Subsets
 * LeetCode: 78
 *
 * Approach: Backtracking
 * ----------------------
 * For every element, we have two choices:
 * 1. Include it in the current subset.
 * 2. Don't include it.
 *
 * Time Complexity: O(n * 2^n)
 * Space Complexity: O(n)
 */

import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        backtrack(nums, 0, current, result);

        return result;
    }

    private void backtrack(
            int[] nums,
            int index,
            List<Integer> current,
            List<List<Integer>> result) {

        if (index == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Include the current element
        current.add(nums[index]);
        backtrack(nums, index + 1, current, result);

        // Don't include the current element
        current.remove(current.size() - 1);
        backtrack(nums, index + 1, current, result);
    }
}
