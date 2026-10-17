// Problem: Number Complement
// LeetCode #476
// Approach: Create a mask of 1s matching the number's binary length, then XOR it with the number.
// Time Complexity: O(1)
// Space Complexity: O(1)

class Solution {
    public int findComplement(int num) {
        if (num == 0) return 1;

        int bitLength = Integer.toBinaryString(num).length();
        
        int mask = (1 << bitLength) - 1;
        
        return num ^ mask;
    }
}
