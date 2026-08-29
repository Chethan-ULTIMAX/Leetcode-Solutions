/*
 * Problem: Diagonal Traverse
 * LeetCode: 498
 *
 * Approach: Store Elements by Diagonal
 * -----------------------------------
 * Elements belonging to the same diagonal have
 * the same value of (row + column).
 *
 * First, calculate the size of every diagonal,
 * store the elements, and then traverse the
 * diagonals in alternating directions.
 *
 * Time Complexity: O(m × n)
 * Space Complexity: O(m × n)
 */

class Solution {

    public int[] findDiagonalOrder(int[][] mat) {

        int rows = mat.length;
        int cols = mat[0].length;

        int diagonalCount = rows + cols - 1;

        int[][] diagonals = new int[diagonalCount][];
        int[] sizes = new int[diagonalCount];

        // Find the size of every diagonal.
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sizes[i + j]++;
            }
        }

        // Create each diagonal.
        for (int i = 0; i < diagonalCount; i++) {
            diagonals[i] = new int[sizes[i]];
        }

        // Store matrix elements in their diagonals.
        int[] index = new int[diagonalCount];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                diagonals[i + j][index[i + j]] = mat[i][j];
                index[i + j]++;
            }
        }

        // Build the final answer.
        int[] result = new int[rows * cols];
        int position = 0;

        for (int i = 0; i < diagonalCount; i++) {

            if (i % 2 == 0) {
                for (int j = diagonals[i].length - 1; j >= 0; j--) {
                    result[position++] = diagonals[i][j];
                }
            } else {
                for (int j = 0; j < diagonals[i].length; j++) {
                    result[position++] = diagonals[i][j];
                }
            }
        }

        return result;
    }
}
