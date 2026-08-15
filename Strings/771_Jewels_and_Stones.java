/*
 * Problem: Jewels and Stones
 * LeetCode: 771
 *
 * Approach: Character Counting
 * ----------------------------
 * For each jewel, count how many times it
 * appears in the stones string.
 *
 * Time Complexity: O(j × s)
 * Space Complexity: O(1)
 */

class Solution {

    public int numJewelsInStones(String jewels, String stones) {

        int count = 0;

        for (char jewel : jewels.toCharArray()) {
            for (char stone : stones.toCharArray()) {
                if (jewel == stone) {
                    count++;
                }
            }
        }

        return count;
    }
}
