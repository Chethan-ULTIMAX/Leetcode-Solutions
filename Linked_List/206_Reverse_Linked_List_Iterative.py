# Problem: Reverse Linked List
# LeetCode: 206
#
# Approach: Iterative
# -------------------
# Traverse the linked list while reversing the
# direction of each node's next pointer.
# Maintain three pointers:
#   - previous
#   - current
#   - next_node
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
