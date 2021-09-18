class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp_buy[i] means max profit in prices[:i+1] if last action is buy
        # dp_sell[i] means max profit in prices[:i+1] if last action is sell
        # initial dp_buy[0] = -prices[0]  dp_sell[0] = 0
        # dp_buy[i] = max(dp_sell[i-1] - prices[i], dp_buy[i-1])
        # dp_sell[i] = max(dp_buy[i-1] + prices[i] - fee, dp_sell[i-1])
        n = len(prices)
        dp_buy ,dp_sell = [0 for _ in range(n)] , [0 for _ in range(n)]
        dp_buy[0] = -prices[0]

        for i in range(1,n):
            dp_buy[i] = max(dp_sell[i-1] - prices[i], dp_buy[i-1])
            dp_sell[i] = max(dp_buy[i-1] + prices[i] - fee, dp_sell[i-1])
        
        return max(dp_buy[-1],dp_sell[-1])

