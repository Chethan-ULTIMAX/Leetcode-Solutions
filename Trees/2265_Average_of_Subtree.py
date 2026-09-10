# Problem: Average of Subtree
# LeetCode: 2265
#
# Approach: Tree Traversal
# -----------------------
# For every node, calculate the sum and number of nodes
# in its subtree using recursive traversal.
#
# Then calculate the integer average of the subtree and
# check whether it is equal to the current node's value.
#
# The tree is traversed again to check every node.
#
# Time Complexity: O(n²)
# Space Complexity: O(h)
#
# n = number of nodes
# h = height of the tree

class Solution(object):
    def averageOfSubtree(self, root):

        def avg(root, c):
            if not root:
                return (0, 0)

            left = avg(root.left, c + 1)
            right = avg(root.right, c + 1)

            total = root.val + left[0] + right[0]
            count = 1 + left[1] + right[1]

            return (total, count)

        def m(root):
            if not root:
                return 0

            total, count = avg(root, 0)
            average = total // count

            ans = 0

            # Check whether the node equals its subtree average.
            if root.val == average:
                ans += 1

            ans += m(root.left)
            ans += m(root.right)

            return ans

        return m(root)
