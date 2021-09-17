class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # minimum delete sum = sum - 2 * max(LCS sum)
        # dp[i][j] means max LCS sum in s1[:i] , s2[j]
        # dp[i][j] = dp[i-1][j-1] + ord(s1[i]) if s1[i] == s2[j] else max(dp[i-1][j], dp[i][j-1])
        
        m , n = len(s1) , len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        maxLsum = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
                maxLsum = max(maxLsum, dp[i][j])
        
        totalsum = sum([ord(ch) for ch in s1 + s2]) 
        return totalsum - 2 * maxLsum




 
