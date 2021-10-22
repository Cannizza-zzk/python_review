class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # dp[i] means problity to get i points
        # dp[i] = sum(dp[i-k]*(1/maxPts) where k in range(1, maxPts))
        # improve:
        # maintain a sliding window 
        # dp[i] = sum(dp[window start:window end]) * basicprob 
        
        if k == 0:
            return 1
        if n == 0:
            return 0
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1

        basicProb = 1 / maxPts
        SumWindow = 1

        for i in range(1, n+1):
            dp[i] = SumWindow * basicProb
            if i < k:
                SumWindow += dp[i]
            if  i - maxPts >= 0 and i - maxPts < k:
                SumWindow -= dp[i - maxPts]
            

        ans  = sum(dp[k:n+1])
        #print(dp)
        return ans