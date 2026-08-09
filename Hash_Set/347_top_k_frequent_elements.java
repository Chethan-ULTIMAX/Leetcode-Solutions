// Problem: Top K Frequent Elements
// LeetCode: 347
//
// Approach: HashMap + Sorting
// ---------------------------
// Count the frequency of each number using a HashMap.
// Store all unique numbers in a list.
// Sort the list based on frequency in descending order.
// Take the first k elements.
//
// Time Complexity: O(n log n)
// Space Complexity: O(n)

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();

        // Count the frequency of each number
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Store all unique numbers
        List<Integer> ans = new ArrayList<>(freq.keySet());

        // Sort numbers by frequency in descending order
        ans.sort((a, b) -> freq.get(b) - freq.get(a));

        // Store the top k frequent elements
        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = ans.get(i);
        }

        return result;
    }
}
