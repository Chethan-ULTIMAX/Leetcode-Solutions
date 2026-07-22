# Problem: String Compression
# LeetCode: 443
#
# Approach: Two Pointers
# ----------------------
# Use one pointer to read consecutive groups of
# identical characters and another pointer to
# write the compressed result in-place.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        read = 0
        write = 0
        n = len(chars)

        while read < n:
            current = chars[read]
            count = 0

            while read < n and chars[read] == current:
                count += 1
                read += 1

            chars[write] = current
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
