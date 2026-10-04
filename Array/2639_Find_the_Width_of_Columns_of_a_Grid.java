// Problem: Find the Width of Columns of a Grid
// LeetCode #2639
// Approach: Find the number of digits in each value and store the maximum width for every column.
// Time Complexity: O(m * n * d), where d is the number of digits in a number.
// Space Complexity: O(n)

class Solution {
    public int[] findColumnWidth(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] rez = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                int len = getLen(grid[i][j]);

                if (rez[j] < len) {
                    rez[j] = len;
                }

            }
        }

        return rez;
    }

    private int getLen(int num) {
        int len = num <= 0 ? 1 : 0;

        while (num != 0) {
            num /= 10;
            len++;
        }

        return len;
    }
}
