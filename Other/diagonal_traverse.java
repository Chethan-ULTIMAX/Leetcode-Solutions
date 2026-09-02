class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int row = mat.length;
        int col = mat[0].length;

        int m = row + col - 1;

        // Create diagonals
        int[][] diag = new int[m][];

        // Find size of every diagonal
        int[] size = new int[m];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                size[i + j]++;
            }
        }

        // Create each diagonal array
        for (int i = 0; i < m; i++) {
            diag[i] = new int[size[i]];
        }

        // Put elements into diagonals
        int[] index = new int[m];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                diag[i + j][index[i + j]] = mat[i][j];
                index[i + j]++;
            }
        }

        // Create final answer
        int[] arr = new int[row * col];
        int k = 0;

        for (int i = 0; i < m; i++) {
            int x = diag[i].length;

            if (i % 2 == 1) {
                for (int j = 0; j < x; j++) {
                    arr[k] = diag[i][j];
                    k++;
                }
            } else {
                for (int j = x - 1; j >= 0; j--) {
                    arr[k] = diag[i][j];
                    k++;
                }
            }
        }

        return arr;
    }
}