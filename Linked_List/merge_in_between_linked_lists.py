class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        res = list1
        temp = list1
        c = 0

        # Find node before a
        while c < a - 1:
            temp = temp.next
            c += 1

        pre = temp

        # Move to node after b
        while c <= b:
            temp = temp.next
            c += 1

        nex = temp

        # Connect list1 -> list2
        pre.next = list2

        # Find end of list2
        temp = list2
        while temp.next:
            temp = temp.next

        # Connect list2 -> remaining list1
        temp.next = nex

        return res