class Solution {
    public void setZeroes(int[][] matrix) {
        int rn = matrix.length;
        int cn = matrix[0].length;

        int[] row = new int[rn];
        int[] col = new int[cn];

        for (int i = 0; i < rn; i++) {
            for (int j = 0; j < cn; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        for (int i = 0; i < rn; i++) {
            if (row[i] == 1) {
                for (int j = 0; j < cn; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int j = 0; j < cn; j++) {
            if (col[j] == 1) {
                for (int i = 0; i < rn; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}