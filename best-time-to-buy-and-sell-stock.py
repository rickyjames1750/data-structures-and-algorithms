class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        res = 0
        min = prices[0]
        for p in prices:
            if min > p:
                min = p
            res = max(res, p-min)
        return res