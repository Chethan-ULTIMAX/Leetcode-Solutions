// Problem: Number of Common Factors
// LeetCode #2427
// Approach: Check every number up to the smaller of a and b.
// Time Complexity: O(min(a, b))
// Space Complexity: O(1)

class Solution {
    public int commonFactors(int a, int b) {
        int total = 0;
        int c = 0;
        if(a > b) c = b;
        else c = a; 
        for(int i = 1; i <= c; ++i)
        {
            if((a % i == 0) && (b % i == 0)) total++;
        }
        return total;
    }
}
