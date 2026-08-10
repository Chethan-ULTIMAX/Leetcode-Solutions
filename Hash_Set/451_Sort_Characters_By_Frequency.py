# Problem: Sort Characters By Frequency
# LeetCode: 451
#
# Approach: Hash Map + Sorting
# ----------------------------
# Count the frequency of each character,
# sort the characters by decreasing frequency,
# and build the result using those frequencies.
#
# Time Complexity: O(n + k log k)
# Space Complexity: O(n + k)
# where k is the number of distinct characters.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        sorted_chars = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        result = ""

        for char in sorted_chars:
            result += char * frequency[char]

        return result
