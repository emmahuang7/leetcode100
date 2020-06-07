class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_price = 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            max_price = max(max_price,prices[i]-min_price)
        return max_price
#动态规划
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0],dp[0][1] = 0,-prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]
