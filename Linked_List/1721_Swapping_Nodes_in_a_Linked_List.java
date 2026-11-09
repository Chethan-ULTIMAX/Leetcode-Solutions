/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        if (head == null || head.next == null) return head;
        ListNode first = head, second = head, mark = head;
        for (int i = 1; i < k; i++) {
            first = first.next;
        }
        mark = first;
        while (first.next != null) {
            second = second.next;
            first = first.next;
        }
        int temp = mark.val;
        mark.val = second.val;
        second.val = temp;
        return head;
    }
}
