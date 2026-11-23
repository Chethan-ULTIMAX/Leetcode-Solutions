/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int averageOfSubtree(TreeNode root) {
        return m(root);
    }

    public int[] avg(TreeNode root) {
        if (root == null) {
            return new int[]{0, 0};
        }

        int[] left = avg(root.left);
        int[] right = avg(root.right);

        int total = root.val + left[0] + right[0];
        int count = 1 + left[1] + right[1];

        return new int[]{total, count};
    }

    public int m(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int[] result = avg(root);

        int total = result[0];
        int count = result[1];

        int average = total / count;

        int ans = 0;

        if (root.val == average) {
            ans++;
        }

        ans += m(root.left);
        ans += m(root.right);

        return ans;
    }
}