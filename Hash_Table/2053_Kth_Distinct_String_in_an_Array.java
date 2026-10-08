// Problem: Kth Distinct String in an Array
// LeetCode #2053
// Approach: Count each string, then scan the array in original order to find the kth string appearing exactly once.
// Time Complexity: O(n)
// Space Complexity: O(n)

import java.util.HashMap;

class Solution {
    public String kthDistinct(String[] arr, int k) {
        HashMap<String,Integer> map = new HashMap<>();
        for(String s:arr){
            if(map.containsKey(s))
                map.put(s,map.get(s)+1);
            else
                map.put(s,1);
        }
        int c=0;
        for(String s : arr) {
            if(map.get(s) == 1) {
                c++;
                if(c == k)
                    return s;
            }
        }
        return "";
    }
}
