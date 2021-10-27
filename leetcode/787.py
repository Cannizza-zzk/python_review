class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp[i][j] means cheapest prices from i to dst with j stops
        # dp[i][j] = min(dp[next_i][j-1] + price)
        # dp[dst][:] = 0
        # dp[i][0] = math.inf if i cannot reach dst else price_i_dst
        import math
        fprice = [[math.inf for _ in range(n)] for _ in range(n)]
        for flight in flights:
            fprice[flight[0]][flight[1]] = flight[2]

        dp = [[-1 for i in range(k + 1)] for _ in range(n)]

        def find_dp(i, j):
            
            if dp[i][j] != -1:
                return dp[i][j]

            # basic
            if i == dst:
                dp[i][j] = 0
                return dp[i][j]
            if j == 0:
                dp[i][j] = fprice[i][dst]
                return dp[i][j]

            for next_stop, price in enumerate(fprice[i]):
                if price != math.inf:
                    dp[i][j] = price + find_dp(next_stop, j - 1) if dp[i][j] == -1 else min(dp[i][j], price + find_dp(next_stop, j-1))
            
            if dp[i][j] == -1:
                dp[i][j] = math.inf
            
            return dp[i][j]

        ans = find_dp(src,k)
        
        if ans == math.inf:
            return -1
        else:
            return ans
            
