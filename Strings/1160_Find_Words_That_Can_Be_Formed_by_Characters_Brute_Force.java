/*
 * Problem: Find Words That Can Be Formed by Characters
 * LeetCode: 1160
 *
 * Approach: Brute Force Character Counting
 * ----------------------------------------
 * For each word, compare the frequency of every
 * character in the word with its frequency in
 * the given character string. If every character
 * is available, add the word's length to the answer.
 *
 * Time Complexity: O(n × m²)
 * Space Complexity: O(1)
 */

class Solution {

    public int countCharacters(String[] words, String chars) {

        int totalLength = 0;

        for (String word : words) {

            boolean canForm = true;

            for (int i = 0; i < word.length(); i++) {

                char current = word.charAt(i);

                if (count(word, current) > count(chars, current)) {
                    canForm = false;
                    break;
                }
            }

            if (canForm) {
                totalLength += word.length();
            }
        }

        return totalLength;
    }

    private int count(String text, char target) {

        int frequency = 0;

        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == target) {
                frequency++;
            }
        }

        return frequency;
    }
             }
