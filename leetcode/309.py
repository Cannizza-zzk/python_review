class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold , cooldown , nothold = -prices[0] , float('-inf'), 0
        for i in range(len(prices)):
            hold, cooldown, nothold = max(hold, nothold - prices[i]) , hold + prices[i] , max(cooldown, nothold)

        return max(nothold, cooldown)



# reference : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)



# dfs solution time limit exceeded
""" class Solution:
    def __init__(self) -> None:
        self.mProf = 0
        self.prices = []
        self.prof_rcd = {}

    def dfs(self, day_num, prof_now, can_buy, have_stock):
        # basic situation
        if day_num == len(self.prices) - 1:
            self.mProf = max(prof_now + self.prices[day_num], self.mProf) if have_stock else max(prof_now, self.mProf)
            return 

        # today buy
        if (not have_stock) and can_buy:
            self.dfs(day_num+1, prof_now - self.prices[day_num], False, True)
        
        # today sell
        if have_stock:
            self.dfs(day_num+1, prof_now + self.prices[day_num], False, False)
        
        # do nothing
        self.dfs(day_num+1, prof_now, True, have_stock)

        return 


    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        
        self.dfs(0, 0, True, False)

        return self.mProf """