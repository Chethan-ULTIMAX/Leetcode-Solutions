# Problem: Circle and Rectangle Overlapping
# LeetCode: 1401
#
# Approach: Closest Point
# -----------------------
# Find the point inside the rectangle that is closest
# to the center of the circle.
#
# If the squared distance between this closest point
# and the circle's center is less than or equal to
# the squared radius, the circle and rectangle overlap.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def checkOverlap(self, r: int, cx: int, cy: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        # Find the closest point in the rectangle to the circle center.
        x = max(x1, min(cx, x2)) - cx
        y = max(y1, min(cy, y2)) - cy

        # Compare squared distance with squared radius.
        return x * x + y * y <= r * r
