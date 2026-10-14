// Problem: Divide Array Into Equal Pairs
// LeetCode #2206
// Approach: Count occurrences of each value and ensure every count is even.
// Time Complexity: O(n)
// Space Complexity: O(n)

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean divideArray(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        
        for (int count : counter.values()) {
            if (count % 2 != 0) {
                return false;
            }
        }
        
        return true;
    }
}
