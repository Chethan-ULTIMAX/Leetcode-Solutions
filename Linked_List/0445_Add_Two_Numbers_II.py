class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ""
        temp = l1

        while temp:
            num1 += str(temp.val)
            temp = temp.next

        num2 = ""
        temp = l2

        while temp:
            num2 += str(temp.val)
            temp = temp.next

        ans = str(int(num1) + int(num2))

        dummy = ListNode(0)
        head = dummy

        for i in ans:
            dummy.next = ListNode(int(i))
            dummy = dummy.next

        return head.next
