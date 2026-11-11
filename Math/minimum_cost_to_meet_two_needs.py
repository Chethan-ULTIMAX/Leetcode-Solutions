class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        pairs = min(need1,need2)
        cost = pairs * min(costBoth,cost1+cost2)
        a,b = need1-pairs,need2-pairs
        cost += (a * min(cost1,costBoth)) + (b * min(cost2,costBoth))
        return cost
