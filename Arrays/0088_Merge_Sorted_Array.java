// Problem: Merge Sorted Array
// LeetCode: 88
//
// Approach: Two Pointers from the End
// -----------------------------------
// Start from the last valid element of both sorted arrays.
// Place the larger element at the end of nums1.
//
// Working backwards prevents overwriting the elements
// already present in nums1.
//
// Time Complexity: O(m + n)
// Space Complexity: O(1)

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }

            k--;
        }
    }
}
