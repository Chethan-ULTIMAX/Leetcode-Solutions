// Problem: N-Repeated Element in Size 2N Array
// LeetCode: 961
//
// Approach: Adjacent / Near-Duplicate Check
// ------------------------------------------
// The repeated element appears N times in an array of size 2N.
// Therefore, it must appear either next to itself or within
// two positions of itself somewhere in the array.
//
// Check whether A[i] matches A[i + 1] or A[i + 2].
// If a match is found, return that element.
//
// If no match is found, the last element is the repeated one.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int repeatedNTimes(int[] A) {
        for (int i = 0; i < A.length - 2; i++) {
            if (A[i] == A[i + 1] || A[i] == A[i + 2]) {
                return A[i];
            }
        }

        return A[A.length - 1];
    }
}
