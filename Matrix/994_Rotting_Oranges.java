import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.add(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int ans = 0;

        if (fresh == 0) {
            return 0;
        }

        while (!q.isEmpty()) {
            int s = q.size();

            for (int k = 0; k < s; k++) {
                int[] x = q.poll();
                int i = x[0];
                int j = x[1];

                if (i - 1 >= 0 && grid[i - 1][j] == 1) {
                    grid[i - 1][j] = 2;
                    fresh--;
                    q.add(new int[]{i - 1, j});
                }

                if (i + 1 < m && grid[i + 1][j] == 1) {
                    grid[i + 1][j] = 2;
                    fresh--;
                    q.add(new int[]{i + 1, j});
                }

                if (j - 1 >= 0 && grid[i][j - 1] == 1) {
                    grid[i][j - 1] = 2;
                    fresh--;
                    q.add(new int[]{i, j - 1});
                }

                if (j + 1 < n && grid[i][j + 1] == 1) {
                    grid[i][j + 1] = 2;
                    fresh--;
                    q.add(new int[]{i, j + 1});
                }
            }

            if (fresh == 0) {
                return ans + 1;
            }

            ans++;
        }

        return fresh == 0 ? ans : -1;
    }
}
