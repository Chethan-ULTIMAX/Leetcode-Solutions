# Problem: Find All Duplicates in an Array
# LeetCode: 442
#
# Approach: Hash Set
# ------------------
# Traverse the array while keeping track of
# previously seen elements using a set.
# If an element is already present in the set,
# it is a duplicate and is added to the answer.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        seen = set()
        duplicates = []

        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)

        return duplicates
