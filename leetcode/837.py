class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp[i] means problity to get i points
        # dp[i] = sum(dp[i-k]*(1/maxPts) where k in range(1, maxPts))
    
        if k == 0:
            return 1
        if n == 0:
            return 0
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1

        basicProb = 1 / maxPts

        for i in range(1, k):
            start , end = max(0, i-maxPts), i - 1
            dp[i] = sum(dp[start:end+1]) * basicProb

        targ, res = n + 1 , 0
        start , end = max(targ - maxPts, 0), k - 1
        if start > end:
            return 1
        else:
            for i in range(start, end+1):
                res += dp[i] * basicProb * (maxPts - (targ - i) + 1)
                
            return 1 - res

# time limit