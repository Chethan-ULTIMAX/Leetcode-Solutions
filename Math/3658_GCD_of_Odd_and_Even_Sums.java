/*
 * Problem: GCD of Odd and Even Sums
 * LeetCode: 3658
 *
 * Approach: Euclidean Algorithm
 * -----------------------------
 * Compute:
 *   - Sum of first n odd numbers = n²
 *   - Sum of first n even numbers = n(n + 1)
 *
 * Find the GCD of these two values using
 * the Euclidean Algorithm.
 *
 * Time Complexity: O(log(min(a, b)))
 * Space Complexity: O(1)
 */

class Solution {
    public int gcdOfOddEvenSums(int n) {

        int oddSum = n * n;
        int evenSum = n * (n + 1);

        while (evenSum != 0) {
            int remainder = oddSum % evenSum;
            oddSum = evenSum;
            evenSum = remainder;
        }

        return oddSum;
    }
}
