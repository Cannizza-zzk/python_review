class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] means the answer if input is i
        dp = [0 for i in range(n+1)]
        dp[2] , dp[1] = 1 , 1

        for i in range(2,n+1):
            for j in range(2, i):
                dp[i] = max(max(dp[i- j],(i-j)) * max(dp[j],j) , dp[i]) # dp[i - j] means i-j is divided and i-j means use i-j to calculate 
        #print(dp)
        return dp[-1]