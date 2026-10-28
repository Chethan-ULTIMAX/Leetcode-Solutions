class Solution {
    public String stringHash(String s, int k) {
        int summ = 0;
        int t = 0;
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            summ += s.charAt(i) - 'a';
            t++;

            if (t == k) {
                summ %= 26;
                result.append((char) (summ + 'a'));
                summ = 0;
                t = 0;
            }
        }

        return result.toString();
    }
}
