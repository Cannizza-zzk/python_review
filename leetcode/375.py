class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] means minimum amount of money [i , j]
        # dp[i][j] = min(n + max(dp[i][n-1] , dp[n+1][j]))

        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        def cal_range(i,j):
            # basic situation
            if i >= len(dp) or j >= len(dp) or i <= 0 or j <=0:
                return 0
            if i >= j:
                dp[i][j] = 0
            if dp[i][j] != -1:
                return dp[i][j]
                
            for n in range(i,j+1):
                candidate = n + max(cal_range(i,n-1) , cal_range(n+1,j))
                dp[i][j] = candidate if dp[i][j] == -1 else min(candidate,dp[i][j])

            return dp[i][j]

        return cal_range(1,n)
