// Problem: Number of Senior Citizens
// LeetCode #2678
// Approach: Read the age digits from each detail string and count ages greater than 60.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int countSeniors(String[] details) {
        int seniorCount = 0;
        for (String info : details) {
            char tens = info.charAt(11);
            char ones = info.charAt(12);
            if (tens > '6' || (tens == '6' && ones > '0')) {
                seniorCount++;
            }
        }
        return seniorCount;
    }
}
