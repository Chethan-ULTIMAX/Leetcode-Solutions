# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        if not head: return None
        if head.val in nums:
            while head and head.val in nums:
                head = head.next
        if not head: return None

        temp = head
        while temp.next:
            if temp.next.val in nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
