class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] means fewest coins needed to reach amount i
        # dp[i] = min(dp[i-coins[p1]] + 1,...dp[i-coins[pn]]+1)
        dp = [None for _ in range(amount + 1)]
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1 
        dp[0] = 0

        # None for uninitial 
        # -1 for cannnot reach
        def count_coins(i):
            if dp[i] != None:
                return dp[i]

            for coin in coins:
                if coin <= i:
                    candidate = count_coins(i-coin)
                    if candidate != -1:
                        dp[i] = min(candidate+1,dp[i]) if dp[i] != None else candidate + 1
            if dp[i] == None:
                dp[i] = -1

            return dp[i]
        count_coins(amount)
        return dp[-1]


            
        