// Problem: Separate the Digits in an Array
// LeetCode #2553
// Approach: Convert each number to a string, append its digits in order, then copy them into an array.
// Time Complexity: O(total number of digits)
// Space Complexity: O(total number of digits)

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] separateDigits(int[] nums) {
        
        List<Integer> list = new ArrayList<>();

        for (int num : nums) {

            String s = String.valueOf(num);

            for (char ch : s.toCharArray()) {

                list.add(ch - '0');
            }
        }

        int[] result = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }

        return result;
    }
}
