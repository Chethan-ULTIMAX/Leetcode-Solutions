/*
 * Problem: Fizz Buzz
 * LeetCode: 412
 *
 * Approach: Simulation
 * --------------------
 * Iterate from 1 to n.
 * - Add "FizzBuzz" if divisible by both 3 and 5.
 * - Add "Fizz" if divisible by 3.
 * - Add "Buzz" if divisible by 5.
 * - Otherwise, add the number as a string.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<String> fizzBuzz(int n) {

        List<String> result = new ArrayList<>();

        for (int i = 1; i <= n; i++) {

            if (i % 3 == 0 && i % 5 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(String.valueOf(i));
            }
        }

        return result;
    }
}
