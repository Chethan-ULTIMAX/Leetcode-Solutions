// Problem: Search a 2D Matrix
// LeetCode: 74
//
// Approach: Streams + List Search
// -------------------------------
// Convert each row of the 2D array into a List<Integer>.
// Then check each row using contains().
//
// If the target is found in any row, return true.
// Otherwise, return false.
//
// Time Complexity: O(m * n)
// Space Complexity: O(m * n)
//
// m = number of rows
// n = number of columns

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public boolean searchMatrix(int[][] nums, int target) {
        List<List<Integer>> list = Arrays.stream(nums)
                .map(x -> Arrays.stream(x)
                        .boxed()
                        .collect(Collectors.toList()))
                .collect(Collectors.toList());

        for (List<Integer> e : list) {
            if (e.contains(target)) {
                return true;
            }
        }

        return false;
    }
}
