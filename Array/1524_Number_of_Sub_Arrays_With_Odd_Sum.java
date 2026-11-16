class Solution {
    public int numOfSubarrays(int[] arr) {
        int MOD = 1000000007;

        int even = 1;
        int odd = 0;
        int ans = 0;
        int parity = 0;

        for (int num : arr) {
            parity = (parity + num) % 2;

            if (parity == 1) {
                ans = (ans + even) % MOD;
                odd++;
            } else {
                ans = (ans + odd) % MOD;
                even++;
            }
        }

        return ans;
    }
}