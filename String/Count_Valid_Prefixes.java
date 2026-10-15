// Problem: Count Valid Prefixes
// Approach: Track the balance of '1' and other characters in each prefix, counting balances from -1 to 1.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int countValidPrefixes(String s) {
        int cnt = 0, ans = 0;

        for(char ch : s.toCharArray()){
            cnt = ch == '1' ? cnt + 1 : cnt - 1;

            if(cnt >= -1 && cnt <= 1)
                ans++;
        }

        return ans;
    }
}
