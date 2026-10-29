# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        l, temp = 0, head
        while temp:
            temp = temp.next
            l += 1

        pos = l - n
        if pos == 0:
            return head.next

        temp = head
        for i in range(pos - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head
