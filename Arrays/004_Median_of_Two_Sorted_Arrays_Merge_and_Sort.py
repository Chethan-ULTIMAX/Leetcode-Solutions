# Problem: Median of Two Sorted Arrays
# LeetCode: 4
#
# Approach: Merge and Sort
# ------------------------
# Combine both sorted arrays into a single array.
# Sort the merged array.
# If the total number of elements is odd,
# return the middle element.
# Otherwise, return the average of the two
# middle elements.
#
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged = nums1 + nums2
        merged.sort()

        n = len(merged)
        mid = n // 2

        if n % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0

        return merged[mid]
