class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        dp[1], dp[0] = 1, 0

        for i in range(len(dp)):
            for j in range(1,i):
                square = j * j
                if square > i:
                    break
                dp[i] = min(dp[i-square] + 1, dp[i]) if dp[i] != -1 else dp[i-square] + 1

        return dp[-1]

