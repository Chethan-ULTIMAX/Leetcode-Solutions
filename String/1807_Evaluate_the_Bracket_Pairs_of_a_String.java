import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        Map<String, String> mp = new HashMap<>();

        for (List<String> item : knowledge) {
            mp.put(item.get(0), item.get(1));
        }

        StringBuilder key = new StringBuilder();
        StringBuilder res = new StringBuilder();
        boolean flag = false;

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                flag = true;
            } 
            else if (ch == ')') {
                String k = key.toString();

                if (mp.containsKey(k)) {
                    res.append(mp.get(k));
                } 
                else {
                    res.append("?");
                }

                flag = false;
                key.setLength(0);
            } 
            else if (flag) {
                key.append(ch);
            } 
            else {
                res.append(ch);
            }
        }

        return res.toString();
    }
}