/*
 * Problem: Shortest and Lexicographically Smallest Beautiful String
 * LeetCode: 2904
 *
 * Approach: Brute Force
 * ---------------------
 * Start from every possible position and build substrings.
 * Keep track of the number of '1's.
 *
 * Once a substring contains exactly k ones, compare it
 * with the current answer based on:
 * 1. Shorter length
 * 2. Lexicographically smaller value when lengths are equal
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 */

class Solution {

    public String shortestBeautifulSubstring(String s, int k) {

        String answer = "";
        int n = s.length();

        for (int i = 0; i < n; i++) {

            int oneCount = 0;
            StringBuilder current = new StringBuilder();

            for (int j = i; j < n; j++) {

                current.append(s.charAt(j));

                if (s.charAt(j) == '1') {
                    oneCount++;
                }

                if (oneCount > k) {
                    break;
                }

                if (oneCount == k) {

                    String currentString = current.toString();

                    if (answer.isEmpty()
                            || currentString.length() < answer.length()
                            || (currentString.length() == answer.length()
                                && currentString.compareTo(answer) < 0)) {

                        answer = currentString;
                    }
                }
            }
        }

        return answer;
    }
}
