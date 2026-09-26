# Problem: Evaluate the Bracket Pairs in a String
# LeetCode: 1807
#
# Approach: Hash Map + String Traversal
# -------------------------------------
# Store each key-value pair from knowledge in a dictionary.
#
# Traverse the string character by character.
# When '(' is encountered, start collecting the key.
# When ')' is encountered, look up the key in the dictionary.
#
# If the key exists, append its value to the result.
# Otherwise, append '?'.
#
# Characters outside brackets are added directly to the result.
#
# Time Complexity: O(n + k)
# Space Complexity: O(k + r)
#
# n = length of the input string
# k = total size of knowledge
# r = length of the resulting string

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """

        mp = {}

        # Build the key-value mapping.
        for item in knowledge:
            mp[item[0]] = item[1]

        key = ""
        res = ""
        flag = False

        for ch in s:
            if ch == '(':
                flag = True

            elif ch == ')':
                # Replace the key with its value or '?'.
                if key in mp:
                    res += mp[key]
                else:
                    res += "?"

                flag = False
                key = ""

            elif flag:
                key += ch

            else:
                res += ch

        return res
