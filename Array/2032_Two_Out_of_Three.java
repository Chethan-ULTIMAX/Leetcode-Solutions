// Problem: Two Out of Three
// LeetCode #2032
// Approach: Mark values present in each array, then collect values present in at least two arrays.
// Time Complexity: O(n1 + n2 + n3 + 100)
// Space Complexity: O(1) for the fixed-size boolean arrays, excluding the result

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {

        /** Since we have 3 arrays of numbers, 
         * we need 3 boolean arrays.
         *  Here is the length of the longest 
         *  array that can reach the length of the array */
        boolean[] b1 = new boolean[101];
        boolean[] b2 = new boolean[101];
        boolean[] b3 = new boolean[101];

        /** where values of the boolean array 
         * at the corresponding index are changed to true */
        for (int num : nums1) b1[num] = true;

        for (int num : nums2) b2[num] = true;

        for (int num : nums3) b3[num] = true;

        List<Integer> res = new ArrayList<>();


        for (int i = 1; i <= 100; i++){
            if((b1[i] || b2[i]) && (b2[i] || b3[i]) && (b3[i] || b1[i]))
                res.add(i);
        }
        return res;
        
    }
}
