class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        int pairs = Math.min(need1, need2);

        long cost = (long) pairs * Math.min(costBoth, cost1 + cost2);

        int a = need1 - pairs;
        int b = need2 - pairs;

        cost += (long) a * Math.min(cost1, costBoth);
        cost += (long) b * Math.min(cost2, costBoth);

        return cost;
    }
}