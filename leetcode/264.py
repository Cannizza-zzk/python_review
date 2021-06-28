class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp  = [1]
        p1 , p2 , p3 = 0 , 0 , 0
        while len(dp) < n:
            if min(dp[p1]*2, dp[p2]*3, dp[p3]*5) == dp[p1]*2:
                if dp[p1]*2 not in dp:
                    dp.append(dp[p1]*2)
                p1 += 1
            elif min(dp[p1]*2, dp[p2]*3, dp[p3]*5) == dp[p2]*3:
                if dp[p2]*3 not in dp:
                    dp.append(dp[p2]*3)
                p2 += 1
            else:
                if dp[p3] *5 not in dp:
                    dp.append(dp[p3]*5)
                p3 += 1

        return dp[-1]
