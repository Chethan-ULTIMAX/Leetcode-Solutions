# Problem: Merge In Between Linked Lists
# LeetCode: 1669
#
# Approach: Linked List Manipulation
# ----------------------------------
# Find the node before position a and the node
# after position b. Connect the first part of list1
# to list2, then connect the end of list2 to the
# remaining part of list1.
#
# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        current = list1

        # Find the node before position a.
        for _ in range(a - 1):
            current = current.next

        previous = current

        # Find the node after position b.
        for _ in range(b - a + 2):
            current = current.next

        next_node = current

        # Connect list1 to list2.
        previous.next = list2

        # Find the end of list2.
        current = list2

        while current.next:
            current = current.next

        # Connect list2 to the remaining part of list1.
        current.next = next_node

        return list1
