# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr[k-1],arr[-k] = arr[-k],arr[k-1]
        dummy = ListNode(0)
        curr = dummy
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
