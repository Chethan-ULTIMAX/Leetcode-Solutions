import java.util.ArrayList;
import java.util.Stack;

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
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> u = new ArrayList<>();

        while (head != null) {
            u.add(head.val);
            head = head.next;
        }

        int[] nge = new int[u.size()];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < u.size(); i++) {
            while (!stack.isEmpty() && u.get(stack.peek()) < u.get(i)) {
                nge[stack.pop()] = u.get(i);
            }
            stack.push(i);
        }

        return nge;
    }
}
