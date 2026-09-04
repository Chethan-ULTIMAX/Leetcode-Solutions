// Problem: Convert an Array Into a 2D Array With Conditions
// LeetCode: 2610
//
// Approach: Frequency Counting
// -----------------------------
// Keep track of how many times each number has appeared.
// The frequency of a number tells us which row to place
// its next occurrence in. This guarantees that the same
// number never appears twice in the same row.
//
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int[] freq = new int[201];

        for (int num : nums) {
            int row = freq[num]++;

            // Create a new row when required.
            if (row == result.size()) {
                result.add(new ArrayList<>());
            }

            // Add the number to its corresponding row.
            result.get(row).add(num);
        }

        return result;
    }
}
