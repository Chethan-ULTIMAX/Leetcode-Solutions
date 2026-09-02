class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        // Always binary search the smaller array
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;

        int left = 0;
        int right = m;

        while (left <= right) {

            int partition1 = (left + right) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;

            int left1;
            int right1;
            int left2;
            int right2;

            if (partition1 == 0)
                left1 = Integer.MIN_VALUE;
            else
                left1 = nums1[partition1 - 1];

            if (partition1 == m)
                right1 = Integer.MAX_VALUE;
            else
                right1 = nums1[partition1];

            if (partition2 == 0)
                left2 = Integer.MIN_VALUE;
            else
                left2 = nums2[partition2 - 1];

            if (partition2 == n)
                right2 = Integer.MAX_VALUE;
            else
                right2 = nums2[partition2];

            // Correct partition
            if (left1 <= right2 && left2 <= right1) {

                if ((m + n) % 2 == 1) {
                    return Math.max(left1, left2);
                }

                return (Math.max(left1, left2)
                        + Math.min(right1, right2)) / 2.0;
            }

            // We took too many elements from nums1
            else if (left1 > right2) {
                right = partition1 - 1;
            }

            // We took too few elements from nums1
            else {
                left = partition1 + 1;
            }
        }

        return 0.0;
    }
}