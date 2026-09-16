// Problem: Intersection of Two Arrays
// LeetCode: 349
//
// Approach: ArrayList + HashSet
// -----------------------------
// Compare every element of nums2 with every element of nums1.
// If a match is found, add it to an ArrayList.
//
// A HashSet is then used to remove duplicate values.
// Finally, convert the set into an integer array.
//
// Time Complexity: O(m * n)
// Space Complexity: O(m)
//
// m = length of nums1
// n = length of nums2

import java.util.*;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i : nums2) {
            for (int j : nums1) {
                if (i == j) {
                    arr.add(i);
                    break;
                }
            }
        }

        // Remove duplicates.
        Set<Integer> ans = new HashSet<>(arr);

        int[] ans1 = new int[ans.size()];
        int k = 0;

        for (int i : ans) {
            ans1[k++] = i;
        }

        return ans1;
    }
}
